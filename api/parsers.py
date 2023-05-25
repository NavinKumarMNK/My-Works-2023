import binascii
from io import BytesIO
from typing import Dict, Any, Optional, Union
from api.types import Seldonv2InferenceRequest, Input, Parameters
import base64
from PIL import Image

class Parser:
    def __init__(self, inputs:Union[dict, str], parameters:Dict[str, Any] = None):
        self.inputs = inputs
        self.parameters = parameters

    def parse(self):
        raise NotImplementedError("parse() method not implemented in the derived class.")


class ObjectDetectionParser(Parser):
    def is_base64(self, s):
        try:
            # Decoding the provided string using Base64
            decoded_bytes = base64.b64decode(s)
            # Checking if the decoded data starts with common image file headers
            return decoded_bytes.startswith(b'\xff\xd8') or decoded_bytes.startswith(b'\x89PNG')
        except (binascii.Error, ValueError):
            return False
        
    def parse(self) -> Seldonv2InferenceRequest:
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
        if isinstance(s, int):
            return "INT32"
        elif isinstance(s, float):
            return "FP32"
        elif isinstance(s, bool):
            return "BOOL"
        else:
            return "BYTES"

    def parse(self) -> Seldonv2InferenceRequest:
        for key, value in self.parameters.items():
            print (key, type(value))
        
        inputs=[Input(
                name="array_inputs", 
                shape=[-1], 
                datatype="BYTES", 
                data=[self.inputs],
                parameters=Parameters(content_type="str")
            ),
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
        for key, value in self.parameters.items():
            print (key, value)

        return Seldonv2InferenceRequest(
            inputs=[Input(
                name="array_inputs", 
                shape=[-1], 
                datatype="BYTES", 
                data=self.inputs,
                parameters=Parameters(content_type="str")
            ),
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