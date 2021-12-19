import math

s, t = map(float, input().split())


def h(a, b):
    return a / (b ** 2 + 1) + b / (a ** 2 + 1) - (a - b) ** 3


def expression(a, b, max=False):
    if max:
        return a if a > b else b
    return a if a < b else b


ans = h(s, t) + expression(h(s - t, s * t),h(s - t, s + t), True) + h(1, 1)
ans = "{:.2f}".format(ans)
print(ans)
