a = float(input().split(' ')[0])
b = 0
if -1 <= a and a <= 2:
    b = a**2
if a<-1:
    b = 1/a**2
if a > 2:
    b = 4

print("{:.2f}".format(b))

