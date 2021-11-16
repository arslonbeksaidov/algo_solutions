import math

z = input()
array = list(map(float, input().split()))
m = int(input())
i, s = 0, 0

while i < len(array):
    if array[i] < m:
        s += array[i] ** 2
    i += 1

print("{:.0f}".format(s))
