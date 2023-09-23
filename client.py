import argparse
import json
import base64
import os
from kserve import InferRequest, InferInput, InferenceServerClient, InferResponse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--payload', type=str, help='input json file path')
parser.add_argument('--host', type=str, help='Ip address of the gRPC server')
parser.add_argument('--port', type=str, help='Port of the gRPC server')

args = parser.parse_args()

port = args.port
host = args.host
client = InferenceServerClient(
    url=os.environ.get("INGRESS_HOST", host)+":"+os.environ.get("INGRESS_PORT", port),
    channel_args=(('grpc.ssl_target_name_override', os.environ.get("SERVICE_HOSTNAME", "")),)
)

with open(args.payload) as json_file:
    data = json.load(json_file)

data_string = json.dumps(data)

# Encode the data
data_bytes = data_string.encode()
base64_bytes = base64.b64encode(data_bytes)
base64_string = base64_bytes.decode()

# inference
infer_input = InferInput(name="input-0", shape=[1], datatype="BYTES", data=[base64_string])
request = InferRequest(infer_inputs=[infer_input], model_name="model", request_id="1")
res: InferResponse = client.infer(infer_request=request)

if res.outputs[0].contents.bytes_contents[0].decode() == '1':
    print("Predicted Loan Outcome : Repaid ")
elif res.outputs[0].contents.bytes_contents[0].decode() == '0':
    print("Predicted Loan Outcome : Defaulted ")

client.close() 
del client # Unsolvable error
