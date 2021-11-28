from math import *

n, m = map(int, input().split())
matrix = []
for i in range(1, n + 1):
    matrix.append(list(map(int, input().split())))

i = 0
while i < n:
    matrix[i].sort()
    print(" ".join(map(str, matrix[i])))
    i += 1
