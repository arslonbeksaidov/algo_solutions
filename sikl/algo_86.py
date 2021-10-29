import math

a, b, c = map(int, input().split())
x = c
y = 0
while c <= x <= b:
    y += a ** 2 * math.cos(x) + (math.sin(x) / 2) + b * x ** 2
    x += 0.25

print("{:.2f}".format(y))
