import math

z = input()
array = list(map(int, input().split()))
s = 0
i, cnt = 0, 0
while i < len(array):
    if array[i] % 2 != 0:
        s += array[i]
        cnt += 1
    i += 1
print("{:.2f}".format(s / cnt))
