"""if: Where should this line be inserted?"""

import numpy as np

x = np.arange(-5,1)

L = x.ravel() >= 0; # ravel returns a one-dimensional representation of the array

if all(L): print('all x >= 0')
elif any(L): print('at least one x >= 0')
else: print('no x >= 0')

# TASK:
# Where should this line go and what does it do?
# elif sum(L) == 1: print('exactly one x >= 0')

# definitely try it out!
