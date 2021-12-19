import math

a, b = map(float, input().split())


def expression(a, b, max=False):
    if max:
        return a if a > b else b
    return a if a < b else b


ans1 = expression(a, b)
ans2 = expression(a * b, expression(a, b, True))
ans3 = expression(ans1 + ans2, 3.14)
ans = "{:.2f} {:.2f} {:.2f}".format(ans1, ans2, ans3)
print(ans)
