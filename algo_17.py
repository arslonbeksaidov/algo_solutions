import math

input_data = input().split()
x = float(input_data[0])
y = float(input_data[1])

f1 = (2*math.tan(x + math.pi/6))/(1/3 + math.cos(y + x**2)**2)+math.log(x**2 + 2, 2)
print("{:.2f}".format(f1))
