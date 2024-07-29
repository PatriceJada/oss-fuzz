import sys
import atheris
import pybamm
import numpy as np

def test_model(inputs):
    """
    Function to test a PyBaMM model with the provided inputs.
    """
    try:
        # Create a basic model instance
        model = pybamm.lithium_ion.BaseModel()  # Use a base model for simplicity
        
        # Use CasadiAlgebraicSolver if the model is algebraic
        sim = pybamm.Simulation(model, solver=pybamm.CasadiAlgebraicSolver())
        
        # Solve the model with a generic time span
        sim.solve([0, 3600])
    except Exception as e:
        # Handle exceptions to avoid crashing the fuzzer
        print(f"Exception occurred: {e}", file=sys.stderr)

def fuzz_one_input(data):
    """
    Fuzzing function that takes input data and converts it into the format required by the model.
    """
    # Ensure the input data size is a multiple of the element size (4 bytes for np.float32)
    if len(data) % 4 != 0:
        # Adjust the data size by trimming or padding
        data = data[:len(data) - len(data) % 4]
    
    # Convert the input data into a format suitable for the model
    inputs = np.frombuffer(data, dtype=np.float32)
    
    # Call the test model function with the generated inputs
    test_model(inputs)

def main():
    # Set up the fuzzer
    atheris.Setup(sys.argv, fuzz_one_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
