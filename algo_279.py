n = int(input())
a = [[0] * n] * n
i = 0
p = 1
x = 0
y = 0
while i != n * n:
    if x in [0, n] and y in [0, n] and a[x][y] == 0:
        i += 1
        a[x][y] = i
    else:
        p += 1
        if p == 5:
            p = 1
    if p == 1:
        x += 1
    if p == 2:
        y += 1
    if p == 3:
        x -= 1
    if p == 4:
        y -= 1
    print(x, y)

print(a)