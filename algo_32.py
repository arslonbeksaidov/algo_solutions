import math

q = input().split()

x = float(q[0])
y = float(q[1])
z = float(q[2])
print(max(z,max(x,y)),min(z,min(x,y)))
