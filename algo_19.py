import math
input_data = input().split()
x = int(input_data[0])
y = int(input_data[1])

ans = math.log(abs(math.pow(x+y, 2) + math.sqrt(abs(y)+2,) - (x - (x*y / ((x**2 / 2) - 5))))) + \
      math.cos(x + y)**2 / (x + y)**(1/3)

print("{:.2f}".format(ans))
