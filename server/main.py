# author: @NavinKumarMNK
import io
import pandas as pd
from typing import Dict
import base64
import numpy as np
import joblib
import json
from kserve import (
    InferRequest,
    InferResponse,
    InferOutput,
    Model,
    ModelServer
)

class ModelServe(Model):
    def __init__(self, name:str, kmeans_model_path:str, 
                 lgbm_model_path:str):
        super().__init__(name)
        self.model = None
        self.kmeans_model_path = kmeans_model_path
        self.lgbm_model_path = lgbm_model_path
        self.load()
        self.ready = True
        self.threshold = 0.47
    
    def load(self):
        self.kmeans = joblib.load(self.kmeans_model_path)
        self.model = joblib.load(self.lgbm_model_path) # main model
        
    def feature_extractor(self, df):
        def feature_extraction(df):
            df['gps_fix_at'] = pd.to_datetime(df['gps_fix_at'])
            df['server_upload_at'] = pd.to_datetime(df['server_upload_at'])
            
            
            df = df.sort_values(by=['gps_fix_at'])  
            
            if df is None or df.empty:
                return None

            # time difference calc
            df['time_in_out_diff'] = (df['server_upload_at'] - df['gps_fix_at']).dt.total_seconds()
            df['time_gps_fix_shift'] = df['gps_fix_at'].diff().dt.total_seconds()    
            df['time_gps_fix_shift'] = df['time_gps_fix_shift'].fillna(0)
            df['gps_first_server_last_diff'] = (df['server_upload_at'].iloc[-1] - df['gps_fix_at'].iloc[0]).days  
            
            # count location_provider
            location_provider_count = dict(df['location_provider'].value_counts())
            df['location_provider_count_fused'] = location_provider_count.get(0, 0)
            df['location_provider_count_gps'] = location_provider_count.get(1, 0)
            df['location_provider_count_network'] = location_provider_count.get(2, 0)
            df['location_provider_count_local_database'] = location_provider_count.get(3, 0)
            
            # altitude
            zero_count = (df['altitude'] == 0).sum()
            non_zero_count = (df['altitude'] != 0).sum()
            # [0 => city native, 1 => hilly native]
            df['altitude_native'] = 0 if zero_count > non_zero_count else 1
            df['num_travels'] = (df['bearing'] != 0).sum()
            
            # drop "gpu_fix_at", "server_upload_at" columns
            df.drop(columns=["gps_fix_at", "server_upload_at"], inplace=True)
            return df

        df = df.groupby('user_id').apply(feature_extraction).reset_index(drop=True) 
        
        def aggregate_dataframe(df):
            # Handle NaN values
            df = df.fillna(0)

            # Define custom aggregation functions
            def max_(x):
                return np.max(x)
            def min_(x):
                return np.min(x)
            def std_(x):
                return np.std(x) if len(x) > 1 else 0
            def mean_(x):
                return np.mean(x)
            def _(x):
                return int(np.mean(x))

            aggregations = {
                'time_in_out_diff': [max_, min_, std_, mean_],
                'time_gps_fix_shift': [max_, std_, mean_],
                'longitude': [std_],
                'latitude': [std_],
                'altitude': [mean_, std_],
                'bearing': [mean_, std_],
                'location_provider_count_fused': [_],
                'location_provider_count_gps': [_],
                'location_provider_count_network': [_],
                'location_provider_count_local_database': [_],
                'altitude_native': [_],
                'num_travels': [_],
            }

            grouped = df.groupby('user_id')
            df_agg = grouped.agg(aggregations).reset_index()

            # Count occurrences of each cluster for each user_id
            for i in range(24):
                df_agg[f'cluster_{i}_count'] = df.groupby('user_id')['cluster'].apply(lambda x: (x == i).sum()).values

            # Join the multi-level column index into a single-level index
            df_agg.columns = ['_'.join(col).strip() for col in df_agg.columns.values]
            df_agg.rename(columns={'user_id_': 'user_id'}, inplace=True)
            return df_agg

        df_agg = aggregate_dataframe(df)

        
        return df_agg
            
    def predict(self, payload:InferRequest,
                headers:Dict[str, str] = None) -> InferResponse:
        
        # Decoding the payload
        base64_string = payload.inputs[0].data[0]
        decoded_bytes = base64.b64decode(base64_string)
        decoded_string = decoded_bytes.decode()
        data = json.loads(decoded_string)
        
        user_attributes_df = pd.DataFrame(data['user_attributes'], index=[0])
        user_gpx_fixes_df = pd.DataFrame(data['user_gpx_fixes'])

        user_gpx_fixes_df['cluster'] = self.kmeans.predict(user_gpx_fixes_df[['latitude', 'longitude']])
        user_gpx_fixes_df.set_index('id', inplace=True)
        
        df = self.feature_extractor(user_gpx_fixes_df)
        user_attributes_df['user_id'] = data['user_id']
        df = df.merge(user_attributes_df, on='user_id')
        pred = int(self.model.predict_proba(df.drop(columns=['user_id']))[0][1] > self.threshold)
        print(self.model.predict_proba(df.drop(columns=['user_id'])))
        
        infer_output = InferOutput(name="output-0", datatype="BYTES", shape=[1], data=[str(pred)])
        return InferResponse(model_name=self.name, infer_outputs=[infer_output],
                             response_id=payload.id)

    
if __name__ == '__main__':
    model = ModelServe(
        name="model",
        kmeans_model_path="./models/kmeans_model.joblib",
        lgbm_model_path="./models/lgbm.joblib"
    )
    ModelServer().start([model])
    