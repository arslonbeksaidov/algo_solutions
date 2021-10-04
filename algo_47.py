x = float(input())

if x < 0:
    y = -x
if x >=0 and x<=1:
    y = x
if x >=1 and x <=2:
    y =1
if x >=2:
    y  = -2 *x+5

print("{:.2f}".format(y))
