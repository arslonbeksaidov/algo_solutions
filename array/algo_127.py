import math

z = input()
array = list(map(int, input().split()))
i, s = 1, 0
swap_element = min(array) ** 2

while i <= len(array):
    if array[i - 1] < 0:
        array[i - 1] = swap_element
    i += 1

print(" ".join(map(str, array)))
