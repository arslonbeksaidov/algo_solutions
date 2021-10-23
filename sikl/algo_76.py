import math

a, b, c = map(int, input().split())
h = 3
s = 0
for i in range(a, c + 1,  3):
    s += math.pow((a * i + b) / (b * b + math.pow(math.cos(i), 2)), 1 / 3) - math.sin(i * i) / (a * b)

print("{:.2f}".format(s))
