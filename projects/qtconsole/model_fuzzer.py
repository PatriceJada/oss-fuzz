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
