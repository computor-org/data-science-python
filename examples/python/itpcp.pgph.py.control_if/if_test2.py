"""Simple if with and or or"""

a = -1
b = 1

if a > 0 and b > 0:
    print('branch 1: both > 0')
elif a < 0 and b < 0:
    print('branch 1: both < 0')
elif (a < 0 and b > 0) or (a > 0 and b < 0):
    print('branch 1: different signs')
else:
    print('branch 1: at least one is 0')