import math

a, b, c = map(int, input().split())
x = -1
y = 0
while x <= 1:
    y += math.pow((math.sin(a * x) + math.pow(b, c)) / (math.pow(b, 2) + math.pow(math.cos(x), 2)), 1 / 3) - math.sin(x ** 2) / (a * b)
    x += 1/4

print("{:.2f}".format(y))
