def f(n):
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p


x = int(input())

s = 0
p = 1
for i in range(1, x+1):
    if i % 2 != 0:
        s += 1 / f(2 * i - 1)
    else:
        s -= 1 / f(2 * i - 1)

print(format(s, '.4f'))
