import math

a, b, c = map(int, input().split())
x = 1
y = 0
while 1 <= x <= 10:
    y += a * (x * x) / b + x / c
    x += 3

print("{:.2f}".format(y))
