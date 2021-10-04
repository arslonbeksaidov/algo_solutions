import math
n = int(input())
s = 0
for x in range(1,n+1):
    s+=(-1)**(x-1) * math.sin(x**x)/2**x

print("{:.2f}".format(s))
