# Conditional loop
# Danger: infinite loop

n = 10
k = 0

while k <= n:  # as long as condition is true
    print(f"1: k = {k}  n = {n}")
    k += 1
    n -= 1
