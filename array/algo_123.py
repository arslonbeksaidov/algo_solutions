import math

z = input()
array = list(map(int, input().split()))
i, s, n, new_array = 1, 0, 0, []
while i <= len(array):
    if i % 2 == 0:
        s += array[i - 1]
    i += 1

j = 0
while j < len(array):
    if array[j] % 2 != 0 and array[j] > 0:
        new_array.append("{:.2f}".format(array[j] / s))
    else:
        new_array.append("{:.2f}".format(array[j]))
    j += 1

print(" ".join(map(str, new_array)))
