import math

q = input().split()

x = int(q[0])
y = int(q[1])
z = int(q[2])
maxx = max(max(max(x + y + z,x),y),z)
minn = min(min(min(x + y / 2,x),y),z)**2

print("{:.2f}".format(maxx),"{:.2f}".format(minn))
