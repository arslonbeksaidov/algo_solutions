x, y = map(float, input().split())

if y <= x / 2 and x ** 2 + y ** 2 <= 1:
    print('yes')
else:
    print('no')
