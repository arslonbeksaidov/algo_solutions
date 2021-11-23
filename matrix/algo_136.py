n, m = map(int, input().split())
matrix = []
i = 0
while i < n:
    matrix_list = list(map(int, input().split()))
    matrix.append(matrix_list)
    i += 1

removable_index = int(input())

i = 1
while i <= n:
    j = 1
    while j <= m:
        if j == removable_index:
            del matrix[i - 1][j - 1]
        j += 1
    i += 1

i = 0
while i < len(matrix):
    ans = " ".join(map(str, matrix[i]))
    print(ans, end='\n')
    i += 1
