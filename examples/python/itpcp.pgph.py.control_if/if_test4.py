"""if: no matrices allowed in conditions!"""

import numpy as np

x = np.array([-1, 2, 7])

if all(x > 0):
    print('branch 1: all elements > 0')
elif any(x > 0):
    print('branch 1: at least one element > 0')
else:
    print('branch 1: no element > 0')
    