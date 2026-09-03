# Conditional loop
# Danger: infinite loop

n = 3

k = 0
while k < n:
    k += 1
    print(f"1: k = {k}")

# or
k = 0
while True:  # actually forever
    if k >= n:
        break  # Exit
    k += 1
    print(f"2: k = {k}")

# or
k = 0
while True:  # actually forever
    k += 1
    if k >= n:
        break  # Exit
    print(f"3: k = {k}")
