import math

a = int(input())
y = 0
x = - math.pi / 2

while x <= math.pi:
    y += 2 * math.pow(a, math.sin(2 * x) / 3) + x ** 2 * math.cos(a * x)
    x += math.pi / 10

print("{:.2f}".format(y))
