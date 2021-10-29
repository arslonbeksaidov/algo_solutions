import math

a = int(input())
x = 0
y = 0
while 0 <= x <= 10:
    y += a * math.cos(x) - math.sin(x * x)
    x += 0.5

print("{:.2f}".format(y))
