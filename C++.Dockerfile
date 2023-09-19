# Path: MLOps/Rust.Dockerfile

From eclipse/cpp_gcc:latest
ARG DEBIAN_FRONTEND=noninteractive

RUN sudo apt-get update || true
RUN sudo apt-get install emacs -y
RUN sudo apt-get install -y --no-install-recommends \
    apt-transport-https \
    git \
    curl \
    wget \
    vim \
    ca-certificates \
    libjpeg-dev \
    libpng-dev \
    librdmacm1 \
    libibverbs1 \
    libgtk2.0-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    net-tools \
    htop \ 
    && sudo rm -rf /var/lib/apt/lists/*

RUN sudo rm -rf /projects
WORKDIR /workspace

EXPOSE 8080
EXPOSE 5000

RUN sudo chmod -R a+w /workspace
RUN sudo apt-get update

CMD ["tail", "-f", "/dev/null"]
