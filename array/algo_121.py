import math

z = input()
array = list(map(int, input().split()))
m = int(input())
i, s = 1, 0
while i <= len(array):
    if i > m:
        s += array[i - 1]
    i += 1
print("{:.0f}".format(s))
