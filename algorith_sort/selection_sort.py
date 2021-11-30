def selection_sort(array):
    for i in range(len(array)):
        # dastlab birinchi elementini min deb olamiz
        min_index = i
        # siklni ichida array ni birinchi elementidan keyingi elementlarini aylantiramiz
        for j in range(i + 1, len(array)):
            # minimalni topish
            if array[min_index] > array[j]:
                min_index = j
        # har safar arrayni elementini undan keyingi elementlari ichidan topilgan min bilan almashtirib qo'yamiz
        array[i], array[min_index] = array[min_index], array[i]
    return array
