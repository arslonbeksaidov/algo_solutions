import random


def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array.pop(random.randrange(len(array)))
    katta = [i for i in array if i >= pivot]
    kichik = [i for i in array if i < pivot]
    return quick_sort(kichik) + [pivot] + quick_sort(katta)

print(quick_sort([1,2,3,4,5,5,5,5,6,7,8,1,2,3,4,5,21,9,5,4,32,5,6,7,2]))
