import math
n = int(input())
s = 0
for x in range(1,n+1):
    s = s + math.sin(x)/2**x

print("{:.2f}".format(s))
