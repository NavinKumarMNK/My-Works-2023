import json
import httpx
from fastapi import FastAPI
from typing import Dict, Any, Optional, Tuple
from api.seldon import Seldonv2Inference, HuggingFaceSeldonParser
from api.types import HuggingFacePredictRequest
import pprint 

pprint = pprint.pprint
app = FastAPI()

@app.post(path="/predict")
async def predict(request: HuggingFacePredictRequest):
    '''
    @brief : Takes Requets:PredictRequest & converts in v2 Inference Request
             Predict Request is Hugging Face inference API format
             v2 Inference Request is Seldon v2 Inference API format
             Returns the v2 Inference Response

    @param : request: PredictRequest    
    @return: Dict
    '''

    # Convert Hugging Face Request to Seldon v2 Request
    seldon_request: Seldonv2Inference
    model_endpoint: str
    (seldon_request, model_endpoint) = HuggingFaceSeldonParser(request).parsev2()
    pprint(seldon_request.json())

    # Send Seldon v2 Request to Seldon v2 Server
    async with httpx.AsyncClient() as client:
        response = await client.post(model_endpoint, data=seldon_request.json())
        response.raise_for_status()
        return response.json()
    
