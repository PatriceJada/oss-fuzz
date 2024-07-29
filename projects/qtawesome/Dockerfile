# Use the base image for OSS-Fuzz with Python
FROM gcr.io/oss-fuzz-base/base-builder-python

# Install necessary system dependencies
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
    && rm -rf /var/lib/apt/lists/*

# Set up a virtual environment
RUN python3.8 -m venv /qtawesome-env

# Activate the virtual environment and install dependencies
RUN /qtawesome-env/bin/pip install --upgrade pip
RUN /qtawesome-env/bin/pip install qtawesome atheris pyqt5

# Set the environment variables to use the virtual environment
ENV PATH="/qtawesome-env/bin:$PATH"

# Add the current directory to the Docker image and set it as the working directory
ADD . /workspace
WORKDIR /workspace

# Copy the fuzzing target script to the container
COPY model_fuzzer.py /workspace/model_fuzzer.py

# Set the default command to run the fuzzing target in the virtual environment
CMD ["/bin/bash", "-c", "source /qtawesome-env/bin/activate && python model_fuzzer.py"]
