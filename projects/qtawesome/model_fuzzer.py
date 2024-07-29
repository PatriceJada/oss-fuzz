import atheris
import sys
from qtawesome import icon

def FuzzInput(input_data):
    try:
        # Perform some operations with QtAwesome
        icon_name = input_data.decode('utf-8', 'ignore').strip()
        icon(icon_name)
    except Exception as e:
        # Handle exceptions to avoid crashing the fuzzer
        print(f"Exception during fuzzing: {e}", file=sys.stderr)

def main():
    atheris.Setup(sys.argv, FuzzInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
