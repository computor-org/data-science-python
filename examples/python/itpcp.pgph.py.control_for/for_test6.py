# Loop - Modifying loop variable
#      - ugly behavior!
#      - no effect on the loop

n = 5

for k in range(n + 1):
    print(f"1a: k = {k}")
    k = 0
    print(f"1b: k = {k}")
