import atheris
import sys
import pymc as pm
import numpy as np

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    try:
        with pm.Model() as model:
            # Define priors
            mu = pm.Normal("mu", mu=fdp.ConsumeFloatInRange(-10, 10), sigma=1)
            sigma = pm.HalfNormal("sigma", sigma=fdp.ConsumeFloatInRange(0.1, 10))
            
            # Define likelihood
            obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=np.random.randn(100))
            
            # Sample from the model
            trace = pm.sample(10, tune=10)
    except (ValueError, pm.exceptions.SamplingError) as e:
        # Handle specific PyMC sampling errors or value errors
        print(f"Error occurred: {e}")
        return
    except Exception as e:
        # Handle other unexpected exceptions
        print(f"Unexpected error occurred: {e}")
        raise

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
