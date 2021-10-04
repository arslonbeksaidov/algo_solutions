import math
x,y,z  = map(float,input().split())
i = 0;
for number in [x,y,z]:
    if number < 1:
        i += 1


new_array = []
half_sum = 0;
if i == 3:
    minn = min(x,min(y,z))
    for number in [x,y,z]:
        if minn != number:
            half_sum +=number
    for number2 in [x,y,z]:
        if minn == number2:
            number2 = half_sum/2
        new_array.append(number2)
    print(new_array[0],new_array[1],new_array[2])
else:
    print(x,y,z)
