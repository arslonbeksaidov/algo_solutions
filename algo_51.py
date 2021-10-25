x, y = map(float, input().split())

if -1 <= x <= 1 and -2 <= y <= abs(x):
    print('yes')
else:
    print('no')
