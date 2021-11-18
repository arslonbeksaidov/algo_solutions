import math

z = input()
array = list(map(int, input().split()))
i, s, n = 1, 0, 0
while i <= len(array):
    s += array[i - 1] ** 2
    n += array[i - 1]
    i += 1
print("{:.0f}".format(s))
print("{:.2f}".format(n / (i - 1)))
