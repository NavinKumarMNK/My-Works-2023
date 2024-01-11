FROM python:3.9.18-slim-bullseye
ARG DEBIAN_FRONTEND=noninteractive

# Install build essentials
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt


RUN python prefetch.py


ENV TOKENIZERS_PARALLELISM=false
ENV LITERAL_KEY cl_xZM9KkFEVlsrTzhEizi/zUH9m9F9txawfKZIBqCN5JA=

ARG LLAMA_CPP_VERSION=cpu
RUN if [ "$LLAMA_CPP_VERSION" = "gpu" ] ; then CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python; \
    elif [ "$LLAMA_CPP_VERSION" = "metal" ] ; then CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install llama-cpp-python; \
    else pip install --upgrade llama-cpp-python; fi

RUN python credentials.py
EXPOSE 8000
CMD ["chainlit", "run", "app.py"]
