import math

x, y, a, b = map(int, input().split())

S, P, SP = 0, 1, 0

for k in range(1, x + 1):
    S += (k ** 2 + math.sin(k) + 5) / math.pow(k ** 7 + 1, 1 / 5)

for n in range(1, y + 1):
    P *= (n + math.sqrt(n)) / (n - math.pow(n + 1, 1 / 5))

w = 1
while w <= a:
    i = 1
    PP = 1
    while i <= b:
        surat = i ** 2 + math.pow(w, 2 / i)
        maxraj = (math.sin(i) + math.cos(w)) * (i ** w)
        PP *= (surat / maxraj)
        i += 1
    SP += PP
    w += 1

ans = format("{:.2f} {:.2f} {:.2f}".format(S, P, SP))
print(ans)
