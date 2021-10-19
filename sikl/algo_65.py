n, x = map(int, input().split())
s = 0
for i in range(1, n + 1):
    s += i / x ** (2 * i)

print("{:.3f}".format(s))
    
