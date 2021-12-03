from math import *

n, m = map(int, input().split())
matrix = []
for i in range(1, n + 1):
    matrix.append(list(map(int, input().split())))

i = 0
while i < m:
    j = 0
    while j < n - 1:
        ii = j + 1
        while ii < n:
            if matrix[j][i] < matrix[ii][i]:
                first = matrix[j][i]
                second = matrix[ii][i]
                matrix[j][i] = second
                matrix[ii][i] = first
            ii += 1
        j += 1
    i += 1

i = 0
while i < n:
    ans = " ".join(map(str, matrix[i]))
    print(ans)
    i += 1
