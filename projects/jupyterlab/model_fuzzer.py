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

import sys
from jupyterlab_server import LabServerApp
import atheris
import json

def fuzzed_jupyterlab_server(fuzzer_input):
    try:
        # Convert fuzzed input to a string
        input_str = fuzzer_input.decode('utf-8')
        
        # Try to parse it as JSON (simulate an API request or configuration)
        config = json.loads(input_str)
        
        # Start JupyterLab server with fuzzed config
        app = LabServerApp(config=config)
        app.initialize()
        app.start()
        
    except Exception as e:
        # Handle exceptions for any issues
        pass

def main():
    atheris.Setup(sys.argv, fuzzed_jupyterlab_server)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
