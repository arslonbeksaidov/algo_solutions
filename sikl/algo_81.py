import math

a, b = map(int, input().split())
s = 0
x = 1
while x <= 12:
    s += a ** 2 + ((b + math.sin(x))/(a ** 3 + math.cos(x ** 3) * math.cos(x ** 3))) ** (1/5)
    x += 2
print("{:.2f}".format(s))
