
    import math

n, x = map(int, input().split())
s = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        s -= x ** i / math.factorial(i)
    else:
        s += x ** i / math.factorial(i)

print("{:.3f}".format(s))
    
