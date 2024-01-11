# SlabGPT

## Setup - For development
```bash
docker build -t your_image_name -f dev.Dockerfile .
```

Run the container
```bash
docker run -it -p 22:22 -p 8080:8080 -v /path:/app image-name bash
```

## Setup - Production
Before building the container, check the Dockerfile and config.yaml file for changing the environment variables based on the device you are using.

    - build container - make build
    - run container - make run
    - stop container - make stop
    - remove container - make rm
    - remove image - make rmi
    - clean - make clean

## Run Chainlit
```bash
chainlit run app.py -w
```