n = int(input())
matrix = []
i = 0
while i < n:
    matrix_list = list(map(int, input().split()))
    matrix.append(matrix_list)
    i += 1

divider = int(input())

i = 0
cnt = 0
s = 0
while i < n:
    j = 0
    while j < n:
        if matrix[i][j] % divider == 0:
            s += matrix[i][j]
            cnt += 1
        j += 1
    i += 1

print("{:.2f}".format(s / cnt))
