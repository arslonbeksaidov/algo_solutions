def fact(n):
    i = 1
    k = 1
    while i != n + 1:
        k = i * k
        i += 1
    return k

print(fact(5))


def fact_via_recursion(n):
    if n == 1:
        return 1
    else:
        return n * fact_via_recursion(n - 1)


print(fact_via_recursion(5))
