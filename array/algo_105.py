z = input()
array = list(map(int, input().split()))
start, end = map(int, input().split())
sum = 0
cnt = 0
for index, item in enumerate(array):
    if start - 1 > index:
        cnt += 1
        sum += item
    if end - 1 < index:
        cnt += 1
        sum += item

print("{:.2f}".format(sum / cnt))
