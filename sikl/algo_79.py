import math

a = int(input())
x = - math.pi / 2
y = 0
while -math.pi <= x <= math.pi:
    y += math.pow(a, a / 3) + x ** 2 * math.cos(a * x)
    x += math.pi / 19

print("{:.2f}".format(y))
