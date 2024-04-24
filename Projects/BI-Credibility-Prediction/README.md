# Branch-International Credibility Prediction

### Download Dataset
- Setup .env with database credentials
```config
RDS_HOST=xyz.amazonaws.com
PORT=5432
USER=xyz
PASSWORD=xyz
DATABASE=xyz
TABLES=[xyz, yzx, zxy]
```
```bash
python3 scripts/download_data.py
```

## Data Analysis & Modelling
Train Pipeline:
> notebooks/credibity_prediction.ipynb

Test Pipeline:
> notebook/inference_text.ipynb

## Build Server
Build Dockerfile
```bash
docker build -t credibility-prediction .
```

## Run Server
```bash
docker run -p 8080:8080 -p 8081:8081 credibility-prediction
```

## Server on Host without docker
```bash
cd server
python3 main.py
```

## Request GRPC
- Save your Request Json file as payload.json

```bash
python3 client.py --payload payload.json --host docker-container-ip --port docker-container-port
```

## Description
! Note: All scripts are meant to be run from the root directory of the repository. Except for server folder, since it is deployed on Docker container.

