from pydantic import BaseModel, Field, Extra
from typing import Callable, Dict, Any, Optional, Union, List

class HuggingFacePredictRequest(BaseModel):
    hf_pipeline: str
    model_deployed_url: str
    inputs: Optional[Union[dict, str]]
    parameters: Dict[str, Any] = Field(default_factory=dict)
    
class Parameters(BaseModel):
    content_type: str
    headers: Dict[str, Any] = Field(default_factory=dict)
    additionalProp1: Dict[str, Any] = Field(default_factory=dict)
    class Config:
        extra = Extra.allow

class Input(BaseModel):
    name: str
    shape: list
    datatype: str
    parameters: Optional[Union[Parameters, Dict]] = Field(default=Parameters(
                                                    content_type='application/json'
                                                        ))
    data: str

class RequestOutputs(BaseModel):
    name: str
    parameters: Parameters = Field(default_factory=Parameters)

class ResponseOutputs(BaseModel):
    name: str
    shape: list
    datatype: str
    parameters: Optional[Union[Parameters, Dict, None]] = Field(default_factory=None)
    data: List[str]

class Seldonv2InferenceRequest(BaseModel):
    id : str = Field(default=str(''))
    parameters: Optional[Union[Parameters, Dict]] = Field(default=Parameters(
                                                    content_type='application/json'
                                                        ))
    inputs: List[Input]
    outputs: Optional[Union[RequestOutputs, List]] = Field(default_factory=list)

    def dict(self, exclude_unset=True, exclude_none=True, **kwargs):
        return super().dict(
            exclude_unset=exclude_unset, exclude_none=exclude_none, **kwargs
        )

    def json(self, exclude_unset=True, exclude_none=True, **kwargs):
        return super().json(
            exclude_unset=exclude_unset, exclude_none=exclude_none, **kwargs
        )
    
class Seldonv2InferenceResponse(BaseModel):
    model_name: str
    model_version: Optional[Union[str, None]]
    id : str
    parameters: Optional[Union[Parameters, Dict, None]]
    outputs: List[ResponseOutputs]

    def dict(self, exclude_unset=True, exclude_none=True, **kwargs):
        return super().dict(
            exclude_unset=exclude_unset, exclude_none=exclude_none, **kwargs
        )

    def json(self, exclude_unset=True, exclude_none=True, **kwargs):
        return super().json(
            exclude_unset=exclude_unset, exclude_none=exclude_none, **kwargs
        )
    
                            