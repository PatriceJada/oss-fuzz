# Use the base image for OSS-Fuzz with Python
FROM gcr.io/oss-fuzz-base/base-builder-python

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3.8-venv \
    python3.8-dev \
    gfortran \
    libatlas-base-dev \
    graphviz \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

# Set up a virtual environment
RUN python3.8 -m venv /pymc-env

# Activate the virtual environment and install dependencies
RUN /pymc-env/bin/pip install --upgrade pip
RUN /pymc-env/bin/pip install pymc numpy scipy matplotlib pandas atheris

# Set the environment variables to use the virtual environment
ENV PATH="/pymc-env/bin:$PATH"

# Add the current directory to the Docker image and set it as the working directory
ADD . /workspace
WORKDIR /workspace

# Copy the fuzzing target script to the container
COPY model_fuzzer.py /workspace/model_fuzzer.py

# Set the default command to run the fuzzing target in the virtual environment
CMD ["/bin/bash", "-c", "source /pymc-env/bin/activate && python model_fuzzer.py"]


