import math

input_data = input().split()
a = int(input_data[0])
b = int(input_data[1])
c = int(input_data[2])
x = float(input_data[3])

ans = 0.75 + (8.2 * x**2 + math.sqrt(abs(x**3 + 3 * x) + math.cos(x - 2))) / (a / 4 + b / 3 + c / 2 + 1)
print("{:.2f}".format(ans))
