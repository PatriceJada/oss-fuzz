import sys
import atheris
import numpy as np
import cv2
from deepforest import main

def fuzzed_deepforest(input_bytes):
    try:
        # Convert fuzzed input to a numpy array and reshape to a valid image shape
        # We assume an image shape, here (100, 100, 3), as an example
        array_data = np.frombuffer(input_bytes, dtype=np.uint8)
        if len(array_data) < 30000:  # Ensure enough data to form an image
            return

        image = array_data[:30000].reshape((100, 100, 3))

        # Initialize a DeepForest model
        model = main.deepforest()
        model.use_release()

        # Attempt to predict on fuzzed image
        _ = model.predict_image(image=image)
    except Exception as e:
        # Handle exceptions to continue fuzzing
        pass

def main_fuzz():
    atheris.Setup(sys.argv, fuzzed_deepforest)
    atheris.Fuzz()

if __name__ == "__main__":
    main_fuzz()
