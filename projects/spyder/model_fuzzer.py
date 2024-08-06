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
import atheris
from spyder.config.utils import get_filter  

# Define example filetypes for testing
filetypes = [
    ("Python files", ('.py', '.pyw')),
    ("C files", ('.c', '.h')),
    ("Markdown files", ('.md',)),
]

def target_function(data):
    try:
        # Decode the input data to use as the file extension
        ext = data.decode('utf-8')
        # Call the actual function from Spyder's codebase
        result = get_filter(filetypes, ext)
        # Print result for debugging (optional)
        print(f"Filter result for extension '{ext}': {result}")
    except UnicodeDecodeError as e:
        # Handle specific decoding errors and log data
        print(f"UnicodeDecodeError: {e} - Data: {data}")
    except Exception as e:
        # Handle other exceptions and log data
        print(f"Exception occurred: {e} - Data: {data}")

def main():
    # Initialize the fuzzer with the target function
    atheris.Setup(sys.argv, target_function)
    # Start the fuzzing process
    atheris.Fuzz()

if __name__ == "__main__":
    main()
