# Conditional loop - no matrices as condition

import numpy as np

x = np.array([3, -1, -2, 5, -4, 6, 7])

k = 0
# optional: adjust output format
# np.set_printoptions(formatter={'int': lambda i: f'{i:2}'})
print(f"k = {k}, x = {x}")
while np.any(x < 0):  # condition must be a scalar
    if x[k] < 0:
        x[k] = -x[k]
        print(f"k = {k}, x = {x}")
    k += 1
# optional: reset output format to default
# np.set_printoptions()

# This example is of course not smart in practice, since
# the command x = abs(x) yields the same result.
