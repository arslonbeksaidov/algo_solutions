x = float(input())

if x > 1:
    y = x - 1
if x < -1:
    y = -x - 1
if x >=-1 and x <= 0:
    y = x + 1
if 0 <=x and x <=1:
    y = -x+1

print("{:.2f}".format(y))
