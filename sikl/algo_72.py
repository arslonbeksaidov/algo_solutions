import math

n, x = map(int, input().split())
s = 0
for i in range(1, n + 1):
    s += x ** (2 * i - 2) / math.factorial(2 * i - 2)

print("{:.3f}".format(s))
