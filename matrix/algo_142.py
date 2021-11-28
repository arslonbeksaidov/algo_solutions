from math import *

n = int(input())
matrix = []
for i in range(1, n + 1):
    matrix.append(list(map(int, input().split())))

# start, end = map(int, input().split())

i = 0
new_list = []
while i < n:
    j = 0
    while j < n:
        if i <= j:
            new_list.append(matrix[i][j])
        j += 1
    i += 1

print(" ".join(map(str, new_list)))
print(max(new_list), min(new_list))
