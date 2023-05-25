from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, Tuple
from api.types import HuggingFacePredictRequest, Seldonv2InferenceRequest
from api.parsers import PARSE_DICT

class HuggingFaceSeldonParser():
    def __init__(self, request: HuggingFacePredictRequest) :
        self.request = request

    def parsev2(self) -> Tuple[Seldonv2InferenceRequest, str]:
        parser_obj = PARSE_DICT[self.request.hf_pipeline](
            self.request.inputs, self.request.parameters)
        self.seldon_request: Seldonv2InferenceRequest = parser_obj.parse()
        return self.seldon_request, self.request.model_deployed_url
    