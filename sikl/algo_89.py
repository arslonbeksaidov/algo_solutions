import math

a, b, c = map(int, input().split())
y = 0
x = 0
while x <= 1:
    y += math.sqrt((math.sin(a * x) + b ** c) / (b ** 2 + math.cos(x) ** 2)) - math.sin(x ** 2) / (a * b)
    x += 0.25

print("{:.2f}".format(y))
