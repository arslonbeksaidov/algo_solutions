import math
q = input().split()
a = int(q[0])
x = float(q[1])
first = x * math.sin(x/2 + x/3 + x/4)
surat  = math.log10(x**2 - 2) + 3**a
mahraj = math.cos(x + 3) * math.sin(x + 3) + 8
ans = first + surat/mahraj
print("{:.2f}".format(ans))
