import sys
import atheris
import json
from pylsp.config.config import Config

def fuzz_pylsp_config(fuzzer_input):
    try:
        # Convert fuzzed input to string
        input_str = fuzzer_input.decode('utf-8')

        # Parse the input as JSON to simulate configuration input
        config_data = json.loads(input_str)

        # Initialize a Config object with fuzzed data
        config = Config(workspace=None, init_opts=config_data)

        # Access configuration properties (trigger potential bugs)
        config.get('pylsp', {})
    except Exception as e:
        # Handle exceptions and continue
        pass

def main():
    atheris.Setup(sys.argv, fuzz_pylsp_config)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
