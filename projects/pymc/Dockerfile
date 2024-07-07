# Use the OSS-Fuzz base builder image for Python projects
FROM gcr.io/oss-fuzz-base/base-builder-python

# Install Python 3.10 and necessary dependencies for PyMC
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3.10-venv \
    python3.10-dev \
    gfortran \
    libatlas-base-dev \
    graphviz \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment with Python 3.10
RUN python3.10 -m venv /venv

# Install the fuzzer dependencies within the virtual environment
RUN /venv/bin/pip install --upgrade pip setuptools wheel
RUN /venv/bin/pip install numpy scipy matplotlib tables pydot ipython nose hypothesis atheris pymc

# Clone the PyMC repository
RUN git clone https://github.com/pymc-devs/pymc /pymc

# Set FUZZING_LANGUAGE to python
ENV FUZZING_LANGUAGE=python

# Copy the build script and fuzz target
COPY build.sh model_fuzzer.py $SRC/

# Set the working directory
WORKDIR /pymc
