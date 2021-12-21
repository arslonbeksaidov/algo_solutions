def f(n):
    return 0 if n == 0 else (1 if n == 1 else (f(n // 2) if n % 2 == 0 else f(n // 2) + f(n // 2 + 1)))


n = int(input())
print(f(n))
