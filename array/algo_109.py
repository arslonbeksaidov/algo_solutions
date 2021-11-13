import math

z = input()
array = list(map(int, input().split()))
M = int(input())
P = 1
cnt = 0
while cnt < len(array):
    P *= array[cnt] if array[cnt] > M else 1
    cnt += 1

print("{:.2f}".format(math.log(P)))
