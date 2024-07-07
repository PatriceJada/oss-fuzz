import atheris
import sys
import pymc as pm

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    
    try:
        with pm.Model() as model:
            mean = fdp.ConsumeFloat()
            sd = fdp.ConsumeFloat()
            observed_data = fdp.ConsumeIntList(10)
            
            # Define a simple model
            normal_dist = pm.Normal('normal_dist', mu=mean, sigma=sd, observed=observed_data)
            
            # Attempt to sample
            pm.sample(draws=10, tune=10)
    
    except Exception as e:
        if not isinstance(e, (ValueError, TypeError)):
            raise

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
