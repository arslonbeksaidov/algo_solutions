n, m = map(int, input().split())
matrix = []
i = 0
while i < n:
    matrix_list = list(map(int, input().split()))
    matrix.append(matrix_list)
    i += 1

vektor = list(map(int, input().split()))

i = 0
while i < n:
    item = matrix[i][0]
    j = 0
    adding_index = i
    first_element_vektor = vektor[0]
    if item < first_element_vektor:
        adding_index = i
        break
    i += 1

matrix.insert(adding_index, vektor)

i = 0
while i < n + 1:
    ans = " ".join(map(str, matrix[i]))
    print(ans, end="\n")
    i += 1
