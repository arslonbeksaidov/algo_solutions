from math import e
a = map(lambda list1: float(list1), input().split())
obj = list(a)
x = obj[0]
y = obj[1]

ans = ((x + y) / (y**2 + abs((y**2 + 2) / (x + x**3 / 5))))+e **(y+2)

print("{:.2f}".format(ans))
