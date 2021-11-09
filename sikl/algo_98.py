from math import *

x, y, c, d = map(int, input().split())

S, P, SP = 0, 1, 0

for a in range(1, x + 1):
    S += (4 * a + 6 * log(a)) / (a * a + a)

for b in range(1, y + 1):
    P *= abs(b - 6 * cos(b)) / (b * b + b ** (log(b)))

k = 1
while k <= c:
    q = 1
    PP = 1
    while q <= d:
        surat = (q * k + x)
        maxraj = (k ** 2 + y ** 2)
        PP *= surat / maxraj
        q += 1
    SP += PP
    k += 1

ans = format("{:.2f} {:.2f} {:.2f}".format(S, P, SP))
print(ans)
