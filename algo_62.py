 import math
x = int(input())
s = 0
for n in range(1, x + 1):
    if n % 2 == 0:
        s += (-1 ** (n - 1)) * math.sin(n ** n) / 2 ** n
    else:
        s -= (-1 ** (n - 1)) * math.sin(n ** n) / 2 ** n
print("{:.2f}".format(s))
