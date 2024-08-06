# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################

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
