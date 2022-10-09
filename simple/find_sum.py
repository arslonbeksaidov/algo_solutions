
def summa(array):
    if array == []:
        return 0
    return array[0]+summa(array[1:])
