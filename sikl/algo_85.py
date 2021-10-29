import math

a, b, c = map(int, input().split())
x = 1
y = 0
while x <= 20:
    y += (a * x ** 2 + b * x + c) / (a ** 2 + b ** 2 + x ** 2)
    x += 5

print("{:.2f}".format(y))
