# Use the base image for OSS-Fuzz with Python
FROM gcr.io/oss-fuzz-base/base-builder-python

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    gfortran \
    libatlas-base-dev \
    graphviz \
    libhdf5-dev \
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    build-essential \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Set up a virtual environment
RUN python3 -m venv /deepforest-env

# Upgrade pip and install Cython
RUN /deepforest-env/bin/pip install --upgrade pip
RUN /deepforest-env/bin/pip install cython

# Install Deepforest and dependencies
RUN /deepforest-env/bin/pip install numpy pandas matplotlib scikit-learn tensorflow keras deepforest atheris

# Set the environment variables to use the virtual environment
ENV PATH="/deepforest-env/bin:$PATH"

# Add the current directory to the Docker image and set it as the working directory
ADD . /workspace
WORKDIR /workspace

# Copy the fuzzing target script to the container
COPY model_fuzzer.py /workspace/model_fuzzer.py

# Set the default command to run the fuzzing target in the virtual environment
CMD ["/bin/bash", "-c", "source /deepforest-env/bin/activate && python model_fuzzer.py"]
