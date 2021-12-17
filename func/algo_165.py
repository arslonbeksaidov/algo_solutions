import math

t, s = map(float, input().split())


def expression(a, b, c):
    ans = (2 * a - b - math.sin((c))) / (5 + math.fabs(c))
    return float(ans)


ans = "{:.2f}".format(expression(t, -2 * s, 1.17) + expression(2.2, t, s - t))
print(ans)
