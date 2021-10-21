
    import math

n, x = map(int, input().split())
s = 0
for i in range(1, n + 1):
    s += x ** (2 * i - 1) / (2 * i - 1)

print("{:.3f}".format(s))
