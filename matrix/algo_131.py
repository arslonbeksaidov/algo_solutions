matrix_size, matrix_arr_size = map(int, input().split())


def sum_array(list, N):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_array(list[1:], N)


matrix = []
i = 0
new_array = []
while i < matrix_size:
    list_array = list(map(int, input().split()))
    matrix.append(list_array)
    new_array.append(sum_array(list_array, len(list_array)))
    i += 1

k = 0
new_list = []
while k < matrix_arr_size:
    summm = 0
    l = 0
    while l < matrix_size:
        summm += matrix[l][k]
        l += 1
    new_list.append(summm)
    k += 1

i = 0
maxx = float('-inf')
minn = float('inf')
while i < matrix_size:
    j = 0
    m = 0
    while j < matrix_arr_size:
        if maxx < matrix[i][j]:
            maxx = matrix[i][j]
        if minn > matrix[i][j]:
            minn = matrix[i][j]
        j += 1
    i += 1
print(" ".join(map(str, new_list)))
print("{:.0f} {:.0f}".format(maxx, minn))
