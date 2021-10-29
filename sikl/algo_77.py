import math

a, b, c, d = map(int, input().split())
h = 2
s = 0
x = c
while x <= d:
    s += math.pow((math.sin(a * x) + math.pow(b, 2 * c)) / \
                  (b * b + math.pow(math.cos(x), 2)), 1 / 3) - math.sin(x * x) / (
                 a * b)
    x += h

print("{:.2f}".format(s))
