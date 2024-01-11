FROM python:3.9.18-slim-bullseye
ARG DEBIAN_FRONTEND=noninteractive

# Install build essentials
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


COPY . .
VOLUME /app

# By default, install cpu version
RUN pip install --upgrade llama-cpp-python

# Uncomment below line to install gpu version
# RUN CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python

# Uncomment below line to install metal version
# RUN CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install llama-cpp-python

# Run any necessary setup script or prefetching
RUN python prefetch.py

# Expose the necessary port
EXPOSE 8000

# Specify the default command with the '-w' option
CMD ["chainlit", "run", "app.py", "-w"]
