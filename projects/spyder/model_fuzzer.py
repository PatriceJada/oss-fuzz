import sys
import atheris

def target_function(data):
    # This is a dummy function for demonstration
    try:
        input_str = data.decode('utf-8')
        # Simulate some processing
        print(f"Processing input: {input_str}")
    except UnicodeDecodeError as e:
        # Handle specific decoding errors and log data
        print(f"UnicodeDecodeError: {e} - Data: {data}")
    except Exception as e:
        # Handle other exceptions and log data
        print(f"Exception occurred: {e} - Data: {data}")

def main():
    atheris.Setup(sys.argv, target_function)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
