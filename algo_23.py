import math

input_data = input().split()
a = int(input_data[0])
b = int(input_data[1])
c = int(input_data[2])
d = int(input_data[3])
x = float(input_data[4])

if b - c < 0 and a == 0:
    ans = math.cos(abs(a * x + b) / abs(c * x + d + 2**c))
else:
    ans = (a * x**2 + b * x + c) / (x*math.pow(a, 3) + a**2 + a**(b-c)) + math.cos(abs(a * x + b) / abs(c * x + d + 2**c))

print("{:.2f}".format(ans))
