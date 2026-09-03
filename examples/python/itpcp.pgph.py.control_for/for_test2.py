import numpy as np

n = 5
# construct n-by-1 array
x = np.expand_dims(np.arange(n), 1)
for k in x:
    print(f"1: {k}")
# Output:
# 1: [0]
# 1: [1]
# 1: [2]
# 1: [3]
# 1: [4]

# transpose x to use 1-by-n array
for k in x.T:
    print(f"2: {k}")
# Output
# 2: [0 1 2 3 4]

# repeat x to use 3-by-n array
for k in np.repeat(x.T, 3, axis=0):
    print(f"3: {k}")
# Output
# 3: [[0 1 2 3 4]]
# 3: [[0 1 2 3 4]]
# 3: [[0 1 2 3 4]]
