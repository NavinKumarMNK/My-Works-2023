from typing import Dict, Any, Optional, Union
from api.types import Seldonv2InferenceRequest, Input, Parameters

class Parser:
    def __init__(self, inputs:Optional[Union[dict, str]], parameters:Dict[str, Any] = None):
        self.inputs = inputs
        self.parameters = parameters

    def parse(self):
        raise NotImplementedError("parse() method not implemented in the derived class.")


class ObjectDetectionParser(Parser):
    def parse(self) -> Seldonv2InferenceRequest:
        input_type = None
        if isinstance(self.inputs, bytes):
            print("Input string is a bytes.")
            content_type='base64'
        elif isinstance(self.inputs, str):
            print("Input string is a plain string.")
            content_type='str'

        return Seldonv2InferenceRequest(
            inputs=[Input(
                name="array_inputs", 
                shape=[-1], 
                datatype="BYTES", 
                data=self.inputs,
                parameters=Parameters(
                    content_type=content_type,
                )
            )],
         )
        



class TextGenerationParser(Parser):
    def parse(self) -> Seldonv2InferenceRequest:  
        return Seldonv2InferenceRequest(
            inputs=[Input(
                name="array_inputs", 
                shape=[-1], 
                datatype="BYTES", 
                data=self.inputs,
                parameters=Parameters(content_type="str",
                                      headers=self.parameters,
                                      additionalProp1=self.parameters,
                                      **self.parameters)
            )],
            parameters=Parameters(
                    content_type="hg_jsonlist",
                    additionalProp1=self.parameters,
                    **self.parameters
                )
        )
    
class TokenClassificationParser(Parser):
    def parse(self) -> Seldonv2InferenceRequest:
        return Seldonv2InferenceRequest(
            inputs=[Input(
                name="args", 
                shape=[-1], 
                datatype="BYTES", 
                data=self.inputs,
                #parameters=Parameters(
                #    content_type="application/json",
                #    headers=self.parameters,
                #    additionalProp1=self.parameters,
                #    **self.parameters
                #)
            )],
            #parameters=Parameters(
            #        content_type="hg_jsonlist",
            #        headers=self.parameters,
            #        additionalProp1=self.parameters,
            #        **self.parameters
            #    )
        )


class ZeroShotClassificationParser(Parser):
    def parse(self) -> Seldonv2InferenceRequest:
        return Seldonv2InferenceRequest(
            inputs=[Input(
                name="array_inputs", 
                shape=[-1], 
                datatype="BYTES", 
                data=self.inputs,
                parameters=Parameters(
                    content_type="application/json",
                    **self.parameters
                )
            )],
            #parameters=Parameters(
            #        content_type="hg_jsonlist",
            #        headers=self.parameters,
            #        additionalProp1=self.parameters,
            #        **self.parameters
            #    )
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