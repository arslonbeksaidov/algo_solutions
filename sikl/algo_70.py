import math

n, x = map(int, input().split())
s = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        s += x ** (2 * i - 1) / math.factorial(2 * i - 1)
    else:
        s -= x ** (2 * i - 1) / math.factorial(2 * i - 1)

print("{:.3f}".format(s))
