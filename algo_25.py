import math
a,x = map(float,input().split())
a = int(a)

TT = (math.sqrt(x - 1) +\
       math.sqrt(x + 2) + \
        math.log10(math.sqrt(a * x*x) + 2))/(math.sqrt(math.sqrt(x +2) + \
                                            math.sqrt(x + 24) + math.pow(x,5)))
print("{:.2f}".format(TT))
