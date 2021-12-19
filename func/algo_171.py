import math

n = int(input())
x_array = list(map(int, input().split()))
k, m = map(int, input().split())


def sum_array(array, end_index):
    i = 0
    s = 0
    while i < end_index:
        s += array[i]
        i += 1
    return s


ans = (sum_array(x_array, m - k) + sum_array(x_array, k)) / (sum_array(x_array, m) - sum_array(x_array, 4)) ** 2
ans = "{:.2f}".format(ans)
print(ans)
