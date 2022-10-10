def binary_search_via_fact(array, value, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == value:
        return mid
    if array[mid] > value:
        return binary_search_via_fact(array, value, start, mid - 1)
    else:
        return binary_search_via_fact(array, value, mid + 1, end)
    return None


print(binary_search_via_fact([1, 2, 3, 4, 5, 6, 7, 8], 8))
