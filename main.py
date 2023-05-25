import json
import httpx
from fastapi import FastAPI
from typing import Dict, Any, Optional, Tuple
from api.seldon import  HuggingFaceSeldonParser
from api.types import HuggingFacePredictRequest, Seldonv2InferenceRequest, Seldonv2InferenceResponse

app = FastAPI()

@app.post(path="/predict")
async def predict(request: HuggingFacePredictRequest):
    '''
    @brief : Takes Requets:PredictRequest & converts in v2 Inference Request
             Predict Request is Hugging Face inference API format
             v2 Inference Request is Seldon v2 Inference API format
             Returns the v2 Inference Response

    @param : request: HugginFacePredictRequest    
    @return: Json Response
    '''

    # Convert Hugging Face Request to Seldon v2 Request
    seldon_request: Seldonv2InferenceRequest
    model_endpoint: str
    (seldon_request, model_endpoint) = HuggingFaceSeldonParser(request).parsev2()

    # Send Seldon v2 Request to Seldon v2 Server & recive Seldonv2 Response
    async with httpx.AsyncClient() as client:
        response = await client.post(model_endpoint, 
                                data=seldon_request.json(),
                                timeout=60)
        if response.status_code == 200:
            response = Seldonv2InferenceResponse(
                    **response.json()
                )
            return response.outputs[0].data
        elif response.status_code == 500:
            print("Error:", response.text)
        

