import math
x,y,z = map(int,input().split())
a = y + z
b = z + x
c = x + y
if x < a and y < b and z < c:
    print("YES")
else:
    print("NO")
