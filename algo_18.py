import math

input_data = input().split()
x = float(input_data[0])
y = float(input_data[1])

surat = (1/x+(2/x**2)+(3/x**3))+math.e**((x**2)+3*x)
max_raj = math.atan(x+y)+abs(5+x)**2
ans = surat/max_raj - math.cos((y**2)+(x**2)/2)**2
print("{:.2f}".format(ans))
