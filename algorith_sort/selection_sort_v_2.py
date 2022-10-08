def selection_sort(array):
    new_array = []
    for x in range(0, len(array) - 1):
        max_index = find_max(array)
        new_array.append(array.pop(max_index))
    return new_array


def find_max(array):
    max = array[0]
    max_index = 0
    for x in range(1, len(array)):
        if max < array[x]:
            max = array[x]
            max_index = x
    return max_index
