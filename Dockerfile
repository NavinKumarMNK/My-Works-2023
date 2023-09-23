# Use the kserve/sklearnserver base image
FROM kserve/sklearnserver:latest AS kserve-inference

# Set the working directory
WORKDIR /app

# Copy your scikit-learn model file (replace with the actual path)
COPY your_model.pkl /app/your_model.pkl

# Copy your server.py file (replace with the actual path)
COPY server.py /app/server.py

# Install any additional dependencies if needed
# RUN pip install some-package

# Expose the custom gRPC port you defined in server.py (e.g., 6000)
EXPOSE 6000

# Set the entry point to start the gRPC server
CMD ["python", "server.py"]
