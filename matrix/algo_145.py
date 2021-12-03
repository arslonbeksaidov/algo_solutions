n, m = map(int, input().split())


def sum(array, length):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum(array[1:], length)


i = 0
matrix = []
new_list = []
while i < n:
    matrix_list = list(map(int, input().split()))
    summa = sum(matrix_list, len(matrix_list))
    matrix_list.append(summa)
    matrix.append(matrix_list)
    i += 1

for x in matrix:
    ans = " ".join(map(str, x))
    print(ans)
