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

import atheris
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtCore import Qt

# Define a minimal widget class for testing
class TestConsoleWidget(QTextEdit):
    def __init__(self):
        super().__init__()

    def process_input(self, data):
        # For simplicity, we'll use QTextEdit's method for setting text
        self.setPlainText(data.decode('utf-8', 'ignore'))

def fuzz(data):
    app = QApplication(sys.argv)

    # Create an instance of the TestConsoleWidget
    widget = TestConsoleWidget()
    
    # Process the input data
    widget.process_input(data)

def main():
    atheris.Setup(sys.argv, fuzz)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
