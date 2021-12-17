import math

t, s = map(float, input().split())


def expression(a, b):
    ans = (a ** 2 + b ** 2) / (a ** 2 + 2 * a * b + 3 * b ** 2 + 4)
    return float(ans)


ans = "{:.2f}".format(expression(1.2, s) + expression(t, s) + expression(2 * s - 1, s * t))
print(ans)
