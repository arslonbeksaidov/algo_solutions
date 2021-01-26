import math

input_data = input().split()
a = int(input_data[0])
x = float(input_data[1])
y = float(input_data[2])

ans = math.sqrt(math.pow(math.e, x * y) - x * math.sin(a * x) - (x**2 + 2) / (abs(x) + 5)) + math.sqrt(math.log(x**2 + 2) + 5)
print("{:.2f}".format(ans))
