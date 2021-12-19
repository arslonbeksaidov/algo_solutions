import math

a, b, c = map(float, input().split())


def expression(a, b):
    return a if a > b else b


ans = (expression(a, a + b) + expression(a, b + c)) / (1 + expression(a + b * c, 1.15))
ans = "{:.2f}".format(ans)
print(ans)
