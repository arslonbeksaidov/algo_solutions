z = input()
array = list(map(int, input().split()))
sum = 0
minn = float('inf')
for index, item in enumerate(array):
    if minn > item:
        minn = item
new_array = []
cnt = 0
while cnt < len(array):
    item = "{:.2f}".format(array[cnt] / minn)
    new_array.append(item)
    cnt += 1

print(" ".join(new_array))
