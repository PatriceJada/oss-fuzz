# Use the base image for OSS-Fuzz with Python
FROM gcr.io/oss-fuzz-base/base-builder-python

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3.8-venv \
    python3.8-dev \
    build-essential \
    libffi-dev \
    libzmq3-dev \
    libjpeg-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# Set up a virtual environment
RUN python3.8 -m venv /jupyterlab-env

# Activate the virtual environment and install dependencies
RUN /jupyterlab-env/bin/pip install --upgrade pip
RUN /jupyterlab-env/bin/pip install jupyterlab atheris

# Set the environment variables to use the virtual environment
ENV PATH="/jupyterlab-env/bin:$PATH"

# Add the current directory to the Docker image and set it as the working directory
ADD . /workspace
WORKDIR /workspace

# Copy the fuzzing target script to the container
COPY model_fuzzer.py /workspace/model_fuzzer.py

# Set the default command to run the fuzzing target in the virtual environment
CMD ["/bin/bash", "-c", "source /jupyterlab-env/bin/activate && python model_fuzzer.py"]
