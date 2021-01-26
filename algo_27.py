import math

input_data = input().split()
x = float(input_data[0])

ans = math.sqrt((2 * math.tan(x + 2) - math.cos(x + 2**x)) / (1 + math.cos(x + 2)**2)) + math.sin(x**2) / (x**2 + 3)
print("{:.2f}".format(ans))
