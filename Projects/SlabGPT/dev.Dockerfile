FROM python:3.9.18-bullseye
ARG DEBIAN_FRONTEND=noninteractive

# Docker update
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    wget \
    vim \
    ca-certificates \
    libjpeg-dev \
    libpng-dev \
    librdmacm1 \
    libibverbs1 \
    ibverbs-providers \
    libgtk2.0-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    net-tools \
    htop \ 
    && rm -rf /var/lib/apt/lists/*

# Install main dependenices
RUN pip install torch torchvision 'ray[all]' transformers[torch]

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app

EXPOSE 22
EXPOSE 8080

RUN chmod -R a+w /app
RUN apt-get update && apt-get install -y openssh-server

CMD ["tail", "-f", "/dev/null"]