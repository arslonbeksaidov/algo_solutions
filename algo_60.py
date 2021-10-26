x, y = map(float, input().split())

if x ** 2 + y ** 2 <= 1 and x / 2 + 1 >= y >= - x / 2 - 1:
    print("yes")
else:
    print("no")
