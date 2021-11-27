from math import *

n, m = map(int, input().split())
matrix = []
for i in range(1, n + 1):
    matrix.append(list(map(int, input().split())))

i = 0
while i < n:
    j = 0
    while j < m:
        if matrix[i][j] < 0:
            nn, mm = i, j
        j += 1
    i += 1

i = 0
new_matrix = []
while i < n:
    j = 0
    new_list = []
    while j < m:
        if mm != j:
            new_list.append(matrix[i][j])
        j += 1
    if i != nn:
        ans = " ".join(map(str, new_list))
        print(ans, end='\n')
    i += 1
