import math

z = input()
array = list(map(int    , input().split()))
s = 0
i = 1
while i <= len(array):
    if i % 2 != 0:
        s += array[i - 1]
    i += 1
print(s)
