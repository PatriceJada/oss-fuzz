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
import pandas as pd
import numpy as np
from aeon.utils.index_functions import get_time_index, get_index_for_series, get_cutoff, get_window, get_slice

def test_function(data):
    try:
        if data.startswith(b'series'):
            series = pd.Series(np.random.randn(10))
            series.index = pd.date_range('2023-01-01', periods=10)
            get_time_index(series)
            get_index_for_series(series)
            get_cutoff(series)
            get_window(series, 5)
            get_slice(series, 1, 5)
        elif data.startswith(b'array'):
            array = np.random.randn(10)
            get_time_index(array)
            get_index_for_series(array)
            get_cutoff(array)
            get_window(array, 5)
            get_slice(array, 1, 5)
    except Exception as e:
        print(f"Exception: {e}")

def main():
    atheris.Setup(sys.argv, test_function)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
