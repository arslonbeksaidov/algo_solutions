def fact(n):
    i = 1
    k = 1
    while i != n + 1:
        k = i * k
        i += 1
    return k

print(fact(5))
