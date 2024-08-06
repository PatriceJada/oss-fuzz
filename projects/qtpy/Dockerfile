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

# Install necessary system dependencies including Xvfb
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3.8-venv \
    python3.8-dev \
    libgl1-mesa-glx \
    libxcb-xinerama0 \
    libxkbcommon-x11-0 \
    libx11-xcb1 \
    libxcb1 \
    libx11-dev \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libfontconfig1 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set up a virtual environment
RUN python3.8 -m venv /qtpy-env

# Activate the virtual environment and install dependencies
RUN /qtpy-env/bin/pip install --upgrade pip
RUN /qtpy-env/bin/pip install qtpy atheris pyqt5

# Set environment variables for Qt and Xvfb
ENV PATH="/qtpy-env/bin:$PATH"
ENV QT_QPA_PLATFORM=offscreen

# Add the current directory to the Docker image and set it as the working directory
ADD . /workspace
WORKDIR /workspace

# Copy the fuzzing target script to the container
COPY model_fuzzer.py /workspace/model_fuzzer.py

# Run Xvfb and the fuzzer script
CMD ["/bin/bash", "-c", "Xvfb :99 -screen 0 1024x768x24 & source /qtpy-env/bin/activate && export DISPLAY=:99 && python model_fuzzer.py"]
