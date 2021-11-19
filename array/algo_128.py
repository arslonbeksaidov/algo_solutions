z = input()
array = list(map(int, input().split()))
i, s, cnt = 1, 0, 0
while i <= len(array):
    if array[i - 1] % 2 == 0:
        s += array[i - 1]
        cnt += 1
    i += 1

print("{:.2f}".format(s / cnt))
