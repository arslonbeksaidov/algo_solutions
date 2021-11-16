import math

z = input()
array = list(map(float, input().split()))
i, s = 0, 1

while i < len(array):
    if array[i] % 2 == 0 or array[i] % 5 == 0:
        s *= array[i]
    i += 1

print("{:.2f}".format(math.sin(s)))
