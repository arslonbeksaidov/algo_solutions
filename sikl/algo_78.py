import math

a, b, c = map(int, input().split())
h = 2
s = 0
for i in range(a, b + 1, h):
    s += (a ** b + b ** i + c ** a) / (2 * i ** 2 + 3 * a ** i)

print("{:.2f}".format(s))
