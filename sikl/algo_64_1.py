n, x = map(int, input().split())
s = 0
for i in range(1, n+1):
    if i % 2 != 0:
        s += 1 / x ** (2 * i)
    else:
        s -= 1 / x ** (2 * i)

print("{:.3f}".format(s))
