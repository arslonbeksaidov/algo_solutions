from math import *

x, y, c, d = map(int, input().split())

S, P, SP = 0, 1, 0

for a in range(1, x + 1):
    S += (2 * a + cos(a)) ** 2

for b in range(1, y + 1):
    P *= (b + 6) / sqrt(b ** 2 + 2)

k = 1
while k <= c:
    yy = 1
    PP = 0
    while yy <= d:
        surat = k ** 2 + yy
        maxraj = sqrt(k ** 2 + yy ** 2)
        PP += (surat / maxraj)
        yy += 1
    SP += PP
    k += 1

ans = format("{:.2f} {:.2f} {:.2f}".format(S, P, SP))
print(ans)
