import math

n, x = map(int, input().split())
i = 1
s = 0
while i <= n:
    s += x ** i / math.sqrt(i)
    i += 1

print("{:.3f}".format(s))
