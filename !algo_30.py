import math

q = input().split()
x = int(q[0])
y = float(q[1])
z = float(q[2])
ans = math.pow(2,-x) *\
 math.sqrt(x + math.pow(abs(y) + 2,1.0/4)) *\
math.pow((math.pow(math.e,x-1)/ math.sin(z + 2)) + 2,1/3)
print("{:.2}".format(ans))
