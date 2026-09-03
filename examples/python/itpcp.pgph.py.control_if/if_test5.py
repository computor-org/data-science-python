""" Order of conditions is important,
    since only the branch with the first true condition is executed.
"""

a = 2

if a > 0:
    print('1-Zweig: a > 0')
elif a > 1: # branch is never reached
    print('1-Zweig: a > 1')
elif a > 2: # branch is never reached
    print('1-Zweig: a > 2')
else:       # reached when a is less than or equal to zero
    print('1-Zweig: a <= 0')

print(' ')

# Different order necessary!
if a > 2:
    print('2-Zweig: a > 2')
elif a > 1:
    print('2-Zweig: a > 1')
elif a > 0:
    print('2-Zweig: a > 0')
else:
    print('2-Zweig: a <= 0')
    
print(' ')

# or narrowing down the conditions
if a > 0 and a <= 1:
    print('3-Zweig: a > 0')
elif a > 1 and a <= 2:
    print('3-Zweig: a > 1')
elif a > 2:
    print('3-Zweig: a > 2')
else:
    print('3-Zweig: a <= 0')
    
print(' ')

# or multiple conditions, then multiple branches are possible
if a >  0: print('4-Zweig: a > 0')
if a >  1: print('4-Zweig: a > 1')
if a >  2: print('4-Zweig: a > 2')
if a <= 0: print('4-Zweig: a <= 0')


