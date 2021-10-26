x, y = map(float, input().split())
if abs(x) <= y <= 1:
    print('yes')
elif 1 <= y <= 1.5:
    print('yes')
else:
    print('no')
