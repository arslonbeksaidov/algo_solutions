import math

q = input().split()

a = int(q[0])
x = float(q[1])
y = float(q[2])

ans = math.sqrt(y**2 +\
                 math.pow(math.e, x) +\
                  math.sqrt(math.pow(math.e, x) +\
                             a/(x**2 + 2)) +\
                   math.pow(math.cos(x),2) / math.sin(x**2)) + math.pow(math.cos(x),3)
print("{:.2f}".format(ans))
