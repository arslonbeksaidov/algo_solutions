n, m = map(int, input().split())
matrix = []
i = 0
while i < n:
    matrix_list = list(map(int, input().split()))
    matrix.append(matrix_list)
    i += 1

removable_index = int(input())

matrix.pop(removable_index - 1)
i = 0
while i < len(matrix):
    ans = " ".join(map(str, matrix[i]))
    i += 1
    print(ans, end="\n")

