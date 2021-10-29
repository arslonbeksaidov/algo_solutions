import math

a, b, c, d = map(int, input().split())
y = 0
x = d
while x <= c:
    y += math.pow((a * x + b) / ((b ** 2) + math.cos(x) ** 2), 1 / 5) - math.sin(x ** 2) / (a * b)
    x += 1.5

print("{:.2f}".format(y))
