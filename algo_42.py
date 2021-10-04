import math
a,b,c,d = map(float,input().split())
maxx = max(d,max(a,max(b,c)))
minn = min(d,min(a,min(b,c)))
if a <= b <= c <= d :
    print(maxx,maxx,maxx,maxx)
else:
    print(minn,minn,minn,minn)
