import math

input = input().split(" ")
pi = math.pi
s = pi * int(input[1])**2
ans = 1 / 3 * s * int(input[0])
print("{:.2f}".format(ans))
