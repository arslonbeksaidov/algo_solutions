x = input().split()
r1 = int(x[0])
r2 = int(x[1])
r3 = int(x[2])
print("{:.2f}".format((r1*r2*r3)/(r2*r3+r1*r3+r1*r2)))
