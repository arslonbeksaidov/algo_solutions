z = input()
array = list(map(int, input().split()))
new_array = []
minn = min(array)
length = len(array)
for index, item in enumerate(array):
    if item == minn:
        new_last_item = item
        last_item = array[-1]
        array[length - 1] = new_last_item
        array[index] = last_item

print(' '.join([str(elem) for elem in array]))
