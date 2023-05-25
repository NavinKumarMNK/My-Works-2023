# FastAPI Service for Translating Hugging Face Endpoint to Seldon V2 Inference Server Endpoint

This repository contains a FastAPI service that acts as a middleware to translate Hugging Face endpoint request to a Seldon V2 Inference Server Protocol. It allows you to leverage the power of Hugging Face models by seamlessly integrating them with the Seldon platform, server used in TrueFoundry Inferencing Platform.


## Installation & Development

1. Fork & Clone this repository:

   ```bash
   https://github.com/NavinKumarMNK/TrueFoundry-HF-to-v2-API
    ``` 

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the server:

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

4. Unit test the server:

    ```bash
    python test_all.py http://0.0.0.0:8000/predict
    ```

    - Payload Format :

        1. Text Generation
        ```json
        {
            "hf_pipeline": "text-generation",
            "model_deployed_url": "https://text-generation-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/text-generation/infer",
            "inputs": "Hello, how are you today? ",
            "parameters": {
                "min_new_tokens": 10,
                "do_sample": "true",
                "temperature": 1.0,
                "max_new_tokens": 20,
                "num_return_sequences": 5
            }
        }
        ```

        2. Token Classification
        ```json
        {
            "hf_pipeline": "token-classification",
            "model_deployed_url": "https://token-class-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/token-class/infer",
            "inputs": "A 48 year-old female presented with vaginal bleeding and abnormal Pap smears. A 63 year old woman with no known cardiac history presented with a sudden onset of dyspnea requiring intubation and ventilatory support out of hospital. She denied preceding symptoms of chest discomfort, palpitations, syncope or infection. The patient was afebrile and normotensive, with a sinus tachycardia of 140 beats/min.",
            "parameters": {}
        }
        ```

        3. Zero Shot Classification
        ```json
        {
            "hf_pipeline": "zero-shot-classification",
            "model_deployed_url":  "https://zero-shot-class-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/zero-shot-class/infer",
            "inputs": "Last week I upgraded my iOS version and ever since then my phone has been overheating whenever I use your app.",
            "parameters": {
                "candidate_labels": ["mobile", "website", "billing", "account access"]
            }
        }
        ```
        4. Object-Detection
            1. With Url
            ```json
            {
                "hf_pipeline": "object-detection",
                "model_deployed_url": "https://test-object-detect-nikhil-ws.tfy-ctl-euwe1-devtest.devtest.truefoundry.tech/v2/models/test-object-detect/infer",
                "inputs": "https://www.w3.org/WAI/WCAG22/Techniques/pdf/img/table-word.jpg",
                "parameters": {}
            }
            ``` 
            2. With Bytes
            ```json
            {
                "hf_pipeline": "object-detection",
                "model_deployed_url": "https://test-object-detect-nikhil-ws.tfy-ctl-euwe1-devtest.devtest.truefoundry.tech/v2/models/test-object-detect/infer",
                "inputs": "<Base64 Encoding of the image>",
                "parameters": {}
            }
            ```

5. Devlopement
    1. Seldon V2 Inference Request Format for updating custom Models Parser
        - You can add your custom Hugging Face Inference Parser in "/api/parser.py"

        ```python
        class TextGenerationParser(Parser):
            def parse(self) -> Seldonv2InferenceRequest:        
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
            
        ```

    2. Seldon V2 Inference Response Types Correction/ Updataion    
        - You can add/modify you Types replate to the Request & Response in "/api/types.py"
        ```python
        class Input(BaseModel):
            name: str
            shape: List
            datatype: str
            parameters: Optional[Union[Parameters, Dict]] = Field(default=Parameters(content_type='hg_json'))
            data: Union[str, List[str], Image.Image]
            class Config:
                arbitrary_types_allowed = True

        class ResponseOutputs(BaseModel):
            name: str
            shape: list
            datatype: str
            parameters: Optional[Union[Parameters, Dict, None]] = Field(default_factory=Parameters(
                                                            content_type='hg_json'
                                                                ))
            data: List[Union[Dict, List]]

            @validator('data', pre=True)
            def data_to_dict(cls, v):
                dct = []
                for item in v:
                    if isinstance(v, list):
                        dct.append(json.loads(item))
                    else:
                        dct.append(json.loads(item))
                return dct
        ```

    - All above Parsers & Types are Pydantic Models, you can refer to the [Pydantic Docs](https://pydantic-docs.helpmanual.io/) for more details.
    
    
6. Deployment as Docker Container

    ```bash
        # Build the Docker image (from the same directory as the Dockerfile)
        docker build -t my-fastapi-app .

        # Run the Docker container
        docker run -d -p 8000:8000 my-fastapi-app

        # Test it
        curl -X POST -H "Content-Type: application/json" -d '{
            "hf_pipeline": "text-generation",
            "model_deployed_url": "https://text-generation-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/text-generation/infer",
            "inputs": "Hello, how are you today? ",
            "parameters": {
                "min_new_tokens": 10,
                "do_sample": true,
                "temperature": 1.0,
                "max_new_tokens": 20,
                "num_return_sequences": 5
            }
        }' http://<docker-container-ip>:8000/predict

    ```

