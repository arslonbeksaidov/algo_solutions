import math
x = int(input())
s = 0
for x in range(1, x + 1):
    s += math.sin(x) / 2 ** x
print("{:.2f}".format(s))
    
