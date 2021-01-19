import math

x, y = map(float, input().split())
ans = x**(1/5) + (y * (x + y) / (2 * y + x * y))**(1/4) * (x**2 + y**2 + 2)

print("{:.2f}".format(ans))
