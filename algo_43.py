import math
x,y = map(float,input().split())
i = 0
for number in [x,y]:
    if(number < 0):
        i +=1

if i==2:
    print(abs(x),abs(y))
elif i==1:
    print(x + 0.5, y + 0.5)
else:
    print(x,y)
