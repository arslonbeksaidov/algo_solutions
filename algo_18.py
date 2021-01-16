import math as mt

input_data = input().split()

x = float(input_data[0])
y = float(input_data[1])

top = 1/(x+2/x**2 +3/x**3) +  mt.pow(mt.e,x**2 +3*x)

bottom = mt.atan(x+y) + mt.fabs(5 + x)**2

right = mt.cos(y**2 + x**2 / 2) **2

ans = top / bottom - right

print("{:.2f}".format(ans))
