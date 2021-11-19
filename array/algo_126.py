import math


def sum_array(array):
    s = 0
    for i, e in enumerate(array):
        s += e
    return [s, s / (i + 1)]


z = input()
array = list(map(int, input().split()))
i, s = 1, 0
swap_element = "{:.2f}".format(math.log(sum_array(array)[1]))

while i <= len(array):
    if array[i - 1] < 0:
        array[i - 1] = swap_element
    else:
        array[i - 1] = "{:.2f}".format(array[i - 1])
    i += 1

print(" ".join(map(str, array)))
