import math

z = input()
array = list(map(int, input().split()))
k = int(input())
maxx = max(array)
i = 1
while i <= len(array):
    if array[i - 1] == maxx:
        array[i - 1] = array[k - 1]
    i += 1

array[k - 1] = maxx
print(" ".join(map(str, array)))
