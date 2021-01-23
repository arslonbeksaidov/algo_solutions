import math

x1, x2, c, d = map(float, input().split())
c = int(c)
d = int(d)
ans = abs(math.sin(abs(c * x2**3 + d * x1**3 - c * d))**2 / math.sqrt((c * x1**2 + d * x2**2 + 5) + 2)) + math.tan(x1 * x2**2 + d**3)

print("{:.2f}".format(ans))
