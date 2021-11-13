import math

z = input()
array = list(map(int, input().split()))
K, M = map(int, input().split())
P = 1
cnt = 0
while cnt < len(array):
    P *= array[cnt] if array[cnt] == M or array[cnt] == K else 1
    cnt += 1

print("{:.0f}".format(P))
