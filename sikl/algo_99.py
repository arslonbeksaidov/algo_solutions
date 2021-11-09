from math import *

x, y, c, d = map(int, input().split())

S, P, SP = 0, 1, 0

for a in range(1, x + 1):
    S += a ** 3 + e ** a

for b in range(3, y + 1):
    P *= (b * x) / sqrt(b ** 2 + x ** 2)

k = 1
while k <= c:
    q = 1
    PP = 1
    while q <= d:
        surat = k * x + q ** 2
        maxraj = sqrt(k ** 2 + q * y)
        PP *= surat / maxraj
        q += 1
    SP += PP
    k += 1

ans = format("{:.2f} {:.2f} {:.2f}".format(S, P, SP))
print(ans)
