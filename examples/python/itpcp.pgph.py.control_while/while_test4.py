import time

n = 10
k = 0

while k <= n:
    print(k)
    k += 1

print()

k = 0
while True:
    if k > n:
        break
    print(k)
    k += 1

print()

k = 0
while k <= n:
    k += 1
    if n % k != 0:  # even better would be n%k alone
        continue
    print(k)

print()


n = 10**7
s = 0
k = 0

t_start = time.perf_counter()
while k < n:
    s += k
    k += 1

t_while = time.perf_counter() - t_start
print("Sum using while took %.2f seconds!" % (t_while))


s = 0
t_start = time.perf_counter()

for k in range(n):
    s += k

t_for = time.perf_counter() - t_start
print("Sum using for took %.2f seconds!" % (t_for))
