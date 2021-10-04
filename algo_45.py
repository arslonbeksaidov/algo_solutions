import math
a,b,c = map(float,input().split())
d = math.pow(b,2) - 4 * a * c
if d < 0:
    print("NO")
else:
    x1 = (-b +  math.sqrt(b*b - 4 * a * c))/ (2 * a)
    x2 = (-b -  math.sqrt(b*b - 4 * a * c))/ (2 * a)
    print("{:.2f}".format(x1),"{:.2f}".format(x2))
