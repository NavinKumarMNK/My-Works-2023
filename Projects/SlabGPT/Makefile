IMAGE_NAME = slabgpt
CONTAINER_NAME = slabgpt-ctr
DOCKERFILE_PATH = .

build:
	docker build -t $(IMAGE_NAME) $(DOCKERFILE_PATH)

run:
	docker run -v "$(shell pwd):/app" -p 8000:8000 --name slabgpt-ctr -it --rm slabgpt

stop:
	docker stop $(CONTAINER_NAME)

rm:
	docker rm $(CONTAINER_NAME)

rmi:
	docker rmi $(IMAGE_NAME)

clean: stop rm-container rm-image
