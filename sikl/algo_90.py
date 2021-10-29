import math

a, b, c = map(int, input().split())
y = 0
x = -math.pi
while x <= math.pi:
    y += (math.log(a ** (2 * math.sin(x))) + math.exp(2 * x)) / (math.atan(x) + b) + c
    x += math.pi / 10

print("{:.2f}".format(y))
