import math
x,y,z = map(int,input().split())
new_array = []
for x in [x,y,z]:
    if x > 0:
        new_array.append(x**2)
    else:
        new_array.append(x)


a,b,c =map(int,new_array)
print(a,b,c)
