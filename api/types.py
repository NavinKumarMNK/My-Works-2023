from pydantic import BaseModel, Field
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

class Inputs(BaseModel):
    name: str
    shape: list
    datatype: str
    parameters: Optional[Union[Parameters, Dict]] = Field(default_factory=Parameters)
    data: str

class Outputs(BaseModel):
    name: str
    parameters: Parameters = Field(default_factory=Parameters)

class Seldonv2Inference(BaseModel):
    id : str
    parameters: Parameters
    inputs: Inputs
    outputs: Optional[Union[Outputs, List]] 

    def dict(self, exclude_unset=True, exclude_none=True, **kwargs):
        return super().dict(
            exclude_unset=exclude_unset, exclude_none=exclude_none, **kwargs
        )

    def json(self, exclude_unset=True, exclude_none=True, **kwargs):
        return super().json(
            exclude_unset=exclude_unset, exclude_none=exclude_none, **kwargs
        )