import numpy as np
from numpy.core.defchararray import split


nm = input().split()
numpy_array = np.array(split(nm))
print(numpy_array)