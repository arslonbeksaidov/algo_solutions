n, m = map(int, input().split())

matrix = []
for x in range(n):
    matrix_list = list(map(int, input().split()))
    matrix.append(matrix_list)

i = 0
new_list = []
while i < m:
    j = 0
    s = 0
    while j < n:
        s += matrix[j][i]
        j += 1
    new_list.append(s)
    i += 1
matrix.append(new_list)
for x in matrix:
    ans = " ".join(map(str, x))
    print(ans)
