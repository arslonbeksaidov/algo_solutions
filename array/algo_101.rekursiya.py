def sum(list, N):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:], N)


size = int(input())
list = list(map(int, input().split()))

size = len(list)

summa = sum(list, size)

medium = summa / size
sum2 = 0
z = 0
for x in list:
    if medium > x:
        z += 1
        sum2 += x

print("{:.2f}".format(sum2 / z))
