z = input()
array = list(map(float, input().split()))
i, s, cnt = 0, 0, 0

while i < len(array):
    if array[i] < 0:
        s += array[i]
        cnt += 1
    i += 1

print("{:.2f}".format(s / cnt))
