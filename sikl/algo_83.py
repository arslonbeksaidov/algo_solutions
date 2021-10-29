import math

a, b, c = map(int, input().split())
x = 5
y = 0
while x <= 10:
    y += (a ** 2 + b * x + x ** c) / (a ** 2 + b ** 2 + x ** 2)
    x += 0.5

print("{:.2f}".format(y))
