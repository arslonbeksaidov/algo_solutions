import math
x, y = map(float, input().split())


ans = (x**2 + 1)/(x**2 + (x*y + y**2) /
                  (y**2 + (y + x*y) / (abs(x*y) + 5))) + 1 / (1 + math.cos(x) + 1 / math.sin(abs(x)))

print("{:.2f}".format(ans))
