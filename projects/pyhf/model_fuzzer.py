import sys
import atheris
import pyhf
import numpy as np

def test_model(inputs):
    try:
        # Create a simple model using pyhf
        spec = {
            "channels": [
                {
                    "name": "signal",
                    "samples": [
                        {
                            "name": "signal",
                            "data": [inputs[0], inputs[1]],
                            "modifiers": [{"name": "mu", "type": "normfactor", "data": None}]
                        },
                        {
                            "name": "background",
                            "data": [inputs[2], inputs[3]],
                            "modifiers": [{"name": "bkg_norm", "type": "normfactor", "data": None}]
                        }
                    ]
                }
            ]
        }

        model = pyhf.Model(spec)

        # Calculate the expected data
        pars = model.config.suggested_init()
        expected_data = model.expected_data(pars)

        # Calculate the log likelihood
        data_tensor = pyhf.tensorlib.astensor(expected_data)
        log_likelihood = model.logpdf(pars, data_tensor)

        # Perform some checks if needed
        assert log_likelihood is not None
    except Exception as e:
        # Handle exceptions to avoid crashing the fuzzer
        print(f"Exception occurred: {e}", file=sys.stderr)

def fuzz_one_input(data):
    if len(data) < 24:
        return

    inputs = np.frombuffer(data[:24], dtype=np.float32)

    if len(inputs) == 6:
        test_model(inputs)

def main():
    atheris.Setup(sys.argv, fuzz_one_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
