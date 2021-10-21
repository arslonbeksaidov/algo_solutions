import math

n, k = map(int, input().split())
s = 0
for i in range(1, n + 1):
    s += ((-1) ** i * k ** i) / math.factorial(i)
print("{:.3f}".format(s + 1))
