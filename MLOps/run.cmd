docker build -t pytorch -f PyTorch.Dockerfile .
docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -it -v /home/mnk/workspace:/workspace -v /home/mnk/data/:/workspace/data -p 8000:8000 -p 22:22 -p 8080:8080 -p 5000:5000 pytorch bash 
