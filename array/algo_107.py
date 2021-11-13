z = input()
array = list(map(int, input().split()))
sum = 0
maxx = float('-inf')
for index, item in enumerate(array):
    if maxx < item:
        maxx = item
new_array = []
cnt = 0
while cnt < len(array):
    item = "{:.2f}".format(array[cnt] / maxx)
    new_array.append(item)
    cnt += 1

print(" ".join(new_array))
