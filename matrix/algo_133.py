z = int(input())
matrix = []

j = 0
while j < 2:
    i = 0
    while i < z:
        array = list(map(int, input().split()))
        matrix.append(array)
        i += 1
    j += 1

lenth = len(matrix)
middle_index = lenth // 2
first_matrix = matrix[:middle_index]
second_matrix = matrix[middle_index:]

i = 0
while i < z:
    j = 0
    while j < z:
        first_matrix[i].extend(second_matrix.pop(0))
        break
    ans = " ".join(map(str, first_matrix[i]))
    print(ans, end="\n")
    i += 1
