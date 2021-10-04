a, b = map(int, input().split())

max = max(a,b)
minn = min(a,b)
ans1 = (a + b) / 2;
ans2 = 4 * a * b

if a > b:
    b = ans1
    a = ans2
else:
    b = ans2
    a = ans1

print("{:.1f}".format(a),"{:.1f}".format(b))
