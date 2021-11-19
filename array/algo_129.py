import math


def helper_func(array):
    s = 0
    for i, e in enumerate(array):
        s += e
    return [s, s / (i + 1)]


z = input()
array = list(map(int, input().split()))
i, s = 1, 0
while i <= len(array):
    if array[i - 1] % 2 == 0 or array[i - 1] % 3 == 0 or array[i - 1] % 5 == 0:
        s += array[i - 1]
    i += 1

print("{:.0f}".format(s))
