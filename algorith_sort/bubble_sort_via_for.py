def bubble_sort(array):
    n = len(array)
    for x in range(len(array)):
        for y in range(0, n - x - 1):
            if array[y] > array[y + 1]:
                array[y + 1], array[y] = array[y], array[y + 1]
    return array


print(bubble_sort([1, 5, 3, 7, 5, 1, 7]))
