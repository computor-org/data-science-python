# Loop - Iterating through a matrix

import numpy as np

x = np.array([1, 5, 9, 3, 4, 7]).reshape(2, 3)
print(f"x: {x}")

p = 1
for k, v in enumerate(x.ravel()):
    p *= v
    print(f"Index: {k}, Value: {v}, Product: {p}")
