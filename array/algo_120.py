import math

z = input()
array = list(map(int, input().split()))
start, end = map(int, input().split())
s = 0
i, cnt = 0, 0
while i < len(array):
    if start > array[i]:
        cnt += 1
    if end < array[i]:
        cnt += 1
    i += 1
print("{:.0f}".format(cnt))
