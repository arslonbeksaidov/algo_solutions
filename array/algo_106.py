z = input()
array = list(map(int, input().split()))
sum = 0
for index, item in enumerate(array):
    sum += item ** 2

print("{:.0f}".format(sum))
