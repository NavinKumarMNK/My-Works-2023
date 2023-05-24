from typing import Dict, Any, Optional, Union
from api.types import Seldonv2Inference, Inputs

class Parser:
    def __init__(self, inputs:Optional[Union[dict, str]], parameter:Dict[str, Any] = None):
        self.inputs = inputs
        self.parameter = parameter

    def parse(self):
        raise NotImplementedError("parse() method not implemented in the derived class.")


class ObjectDetectionParser(Parser):
    def parse(self):
        def parse(self):
            input_type = None
            if isinstance(self.inputs, bytes):
                input_type = ''
            elif isinstance(self.inputs, str):
                print("Input string is a plain string.")
            else:
                print("Input is not a string.")
        return Seldonv2Inference(output)


class TextClassificationParser(Parser):
    def parse(self):
        '''
        Sample Input{
            "inputs": "This sound track was beautiful! It paints the senery 
                    in your mind so well I would recomend it even to people 
                    who hate vid. game music!"
            }
        '''
        response = dict(
            inputs=["args", [-1], "BYTES", dict(content_type="hg_json"), self.inputs],
            outputs=["outputs", [-1], "BYTES", dict(content_type="hg_json")], 
        )
        return response

class TextGenerationParser(Parser):
    def parse(self) -> Seldonv2Inference:
        '''
        Sample Input{
            "inputs": "This sound track was beautiful! It paints the senery 
                    in your mind so well I would recomend it even to people 
                    who hate vid. game music!"
            }
        '''
        print(self.inputs)
        return Seldonv2Inference(
            id='0',
            parameters=dict(content_type="hg_json"),
            inputs=Inputs(
                name="array_inputs", 
                shape=[-1], 
                datatype="BYTES", 
                parameters=dict(content_type="hg_json"),
                data=self.inputs
                ),
            outputs=[], 
        )

class TextTranslationParser(Parser):
    def parse(self):
        # Text translation parsing logic
        output = self.input1 + self.input2
        return output


class TokenClassificationParser(Parser):
    def parse(self):
        # Token classification parsing logic
        output = self.input1 + self.input2
        return output


class ZeroShotClassificationParser(Parser):
    def parse(self):
        # Zero-shot classification parsing logic
        output = self.input1 + self.input2
        return output


PARSE_DICT = {
    "object-detection" : ObjectDetectionParser,
    "text-classification" : TextClassificationParser,
    "text-generation" : TextGenerationParser,
    "text-translation" : TextTranslationParser,
    "token-classification" : TokenClassificationParser,
    "zero-shot-classification" : ZeroShotClassificationParser,
}

# Usage
if __name__ == "__main__":
    parsers = [
        ObjectDetectionParser("input1", "input2"),
        TextClassificationParser("input1", "input2"),
        TextGenerationParser("input1", "input2"),
        TextTranslationParser("input1", "input2"),
        TokenClassificationParser("input1", "input2"),
        ZeroShotClassificationParser("input1", "input2"),
    ]

    for parser in parsers:
        output = parser.parse()
        print(output)