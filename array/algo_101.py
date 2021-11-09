
    from math import *

size = int(input())
list = list(map(int, input().split()))

size = len(list)

sum = 0
for x in list:
    sum += x
sum = sum / size
sum2 = 0
z = 0
for x in list:
    if sum > x:
        z += 1
        sum2 += x

print("{:.2f}".format(sum2 / z))
