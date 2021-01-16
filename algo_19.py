import math
input_data = input().split()
x = float(input_data[0])
y = float(input_data[1])

z = math.log(abs(math.pow(x+y, 2) + math.pow(abs(y)+2, 0.5) - (x-x*y/(math.pow(x, 2) / 2 - 5)))) + math.cos(x+y)**2 /(x+y)**1/3
print("{:.2f}".format(z))
