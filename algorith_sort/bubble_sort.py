def bubble_sort(array):
    size = len(array)
    # array to'liq sikl aylantirish
    i = 0
    while i < size:
        j = 0
        # maximalni qiymatni o'ng tomonga qo'yib ketadi va iteratsiyani bir ga kamaytirib boradi.
        while j < size - i - 1:
            # maximalnini topish
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1
        i += 1
    return array

array = [99, 2, 3, -5, -1]
ans = bubble_sort(array)
print(ans)
