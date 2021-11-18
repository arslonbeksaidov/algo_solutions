import math

z = input()
array = list(map(int, input().split()))
start, end = map(int, input().split())
i, s = 1, 0
while i <= len(array):
    if start <= i <= end:
        s += array[i - 1] ** 3
    i += 1

print(s)
