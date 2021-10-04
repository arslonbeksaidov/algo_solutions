import math
q = input().split()
a = int(q[0])
b = int(q[1])
c = int(q[2])

if c <=b and b <= a:
    print(2 * a, 2 * b,2 * c)
else:
    print(abs(a),abs(b),abs( c))
