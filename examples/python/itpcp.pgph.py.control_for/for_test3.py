# Loop - Adding, Multiplying

import numpy as np

m = 5
n = 4
x = np.arange(m)

s = np.zeros(m)  # 1×m zero matrix
for k in range(n + 1):
    s += x * k
    print(f"s = {s}")

p = np.ones(m)
for k in range(1, n + 1):
    p *= x * k
    print(f"p = {p}")
