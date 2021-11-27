from math import *

n = int(input())
matrix = []
for i in range(1, n + 1):
    matrix.append(list(map(int, input().split())))
maxx, minn = [], []
i = 0
while i < n:
    j = 0
    while j < n:
        if i == j:
            maxx.append(matrix[i][j])
        j += 1
    i += 1

i = 0
j = n - 1
while i < n:
    while j >= 0:
        minn.append(matrix[i][j])
        break
    j -= 1
    i += 1

print(max(maxx), min(minn))
