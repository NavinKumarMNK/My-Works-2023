import binascii
from io import BytesIO
from typing import Dict, Any, Optional, Union
from api.types import Seldonv2InferenceRequest, Input, Parameters
import base64
from PIL import Image

class Parser:
    "Base Parser Class"
    def __init__(self, inputs:Union[dict, str], parameters:Dict[str, Any] = None):
        self.inputs = inputs
        self.parameters = parameters

    def parse(self):
        raise NotImplementedError("parse() method not implemented in the derived class.")


class ObjectDetectionParser(Parser):
    def is_base64(self, s):
        """
        @brief : Checks if the input is base64 encoded
        @param : s: str
        @return: bool
        """
        
        try:
            decoded_bytes = base64.b64decode(s)
            return decoded_bytes.startswith(b'\xff\xd8') or decoded_bytes.startswith(b'\x89PNG')
        except (binascii.Error, ValueError):
            return False
        
    def parse(self) -> Seldonv2InferenceRequest:
        """
        @brief : Parses the input to Seldonv2InferenceRequest
        @param : None {input & parameter from base class}
        @return: Seldonv2InferenceRequest
        """
        if self.is_base64(self.inputs):
            content_type='pillow_image'
        else:
            content_type='str'
        return Seldonv2InferenceRequest(
            inputs=[Input(
                name="inputs", 
                shape=[-1], 
                datatype="BYTES", 
                data=self.inputs,
                parameters=Parameters(content_type=content_type)
            ),
            ]
         )
        
class TextGenerationParser(Parser):
    def data_type(self, s):
        """
        @brief : Checks the data type of the input
        @param : s: str
        @return: str
        """
        if isinstance(s, int):
            return "INT32"
        elif isinstance(s, float):
            return "FP32"
        elif isinstance(s, bool):
            return "BOOL"
        else:
            return "BYTES"

    def parse(self) -> Seldonv2InferenceRequest: 
        """
        @brief : Parses the input to Seldonv2InferenceRequest
        @param : None {input & parameter from base class}
        @return: Seldonv2InferenceRequest
        """       
        inputs=[Input(
                name="array_inputs", 
                shape=[-1], 
                datatype="BYTES", 
                data=[self.inputs],
                parameters=Parameters(content_type="str")
            ),
            #Parameters of the model
            *[Input(
                name=key,
                shape=[-1],
                datatype=self.data_type(self.inputs),
                data=[value if isinstance(value, bool) == False else "true" if value == True else "false"],
                parameters=Parameters(content_type="hg_json")
            ) for key, value in self.parameters.items()],
            ]
        return Seldonv2InferenceRequest(
            inputs=inputs,  
            parameters=Parameters(content_type="hg_json")     
        )
    
class TokenClassificationParser(Parser):
    def parse(self) -> Seldonv2InferenceRequest:
        """
        @brief : Parses the input to Seldonv2InferenceRequest
        @param : None {input & parameter from base class}
        @return: Seldonv2InferenceRequest
        """ 
        return Seldonv2InferenceRequest(
            inputs=[Input(
                name="args", 
                shape=[-1], 
                datatype="BYTES", 
                data=self.inputs,
            )],
        )
class ZeroShotClassificationParser(Parser):
    def parse(self) -> Seldonv2InferenceRequest:
        """
        @brief : Parses the input to Seldonv2InferenceRequest
        @param : None {input & parameter from base class}
        @return: Seldonv2InferenceRequest
        """
        return Seldonv2InferenceRequest(
            inputs=[Input(
                name="array_inputs", 
                shape=[-1], 
                datatype="BYTES", 
                data=self.inputs,
                parameters=Parameters(content_type="str")
            ), 
            #Parameters of the model
            *[Input( 
                name=key,
                shape=[-1],
                datatype="BYTES",
                data=value,
                parameters=Parameters(content_type="str")
            ) for key, value in self.parameters.items()]
            ],   
            parameters=Parameters(content_type="hs_json") 
        )

PARSE_DICT = {
    "object-detection" : ObjectDetectionParser,
    "text-generation" : TextGenerationParser,
    "token-classification" : TokenClassificationParser,
    "zero-shot-classification" : ZeroShotClassificationParser,
}

# Usage
if __name__ == "__main__":
    for parser in PARSE_DICT.values():
        output = parser.parse()
        print(output)