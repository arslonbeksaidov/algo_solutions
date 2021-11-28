from math import *

n, m = map(int, input().split())
matrix = []
for i in range(1, n + 1):
    matrix.append(list(map(int, input().split())))

start, end = map(int, input().split())

i = 0
s = 0
cnt = 0
while i < n:
    j = 0
    while j < m:
        if start <= matrix[i][j] <= end:
            s += matrix[i][j]
            cnt += 1
        j += 1
    i += 1

print("{:.2f}".format(s / cnt))
