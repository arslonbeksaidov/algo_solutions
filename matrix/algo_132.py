z = input()
array = list(map(int, input().split()))
n, m = map(int, input().split())
if len(array) < n * m:
    i = 0
    addition_zero = (n * m) - len(array)
    while i < addition_zero:
        array.append(0)
        i += 1
elif len(array) > n * m:
    removable_item = len(array) - n * m
    i = 0
    while i < removable_item:
        array.pop()
        i += 1

i = 0
new_matrix = []
while i < n:
    j = 0
    new_list = []
    while j < m:
        new_list.append(array.pop(0))
        j += 1
    new_matrix.append(new_list)
    i += 1
i = 0
while i < n:
    ans = " ".join(map(str, new_matrix[i]))
    print(ans)
    i += 1
