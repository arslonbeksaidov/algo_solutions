x, y = map(float, input().split())

if 4 >= x ** 2 + y ** 2 >= 1 and y >= 0:
    print('yes')
else:
    print('no')
