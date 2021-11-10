z = input()
array = list(map(float, input().split()))
start, end = map(int, input().split())
cnt, s = 0, 0

for i in range(0, len(array)):
    if start <= i <= end:
        cnt += 1
        s += array[i - 1]

print("{:.1f}".format(s / cnt))
