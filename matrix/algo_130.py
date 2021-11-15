n, m = map(int, input().split())
matrix = []
for i in range(1, n + 1):
    matrix.append(list(map(int, input().split())))

new_list = []
maxx = float("-inf")
minn = float("inf")
for x in matrix:
    s = 0
    for y in x:
        s += y
        if maxx < y:
            maxx = y
        if minn > y:
            minn = y
    new_list.append(s)

print(" ".join(map(str, new_list)))
print(maxx, minn)
