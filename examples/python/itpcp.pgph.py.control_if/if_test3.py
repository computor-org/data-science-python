"""Nested if"""

from numpy import sign as sign

a = -1
b = 1

s = sign(a*b)

if s > 0:
    if a > 0:
        print('branch 1: both > 0')
    else:
        print('branch 1: both < 0')
elif s < 0:
    print('branch 1: different signs')
else:
    print('branch 1: at least one is 0')