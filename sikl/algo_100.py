from math import *

x, y, c, d = map(int, input().split())

S, P, SP = 0, 1, 1

for a in range(1, x + 1):
    S += (a * x + 4) / sqrt(a + log(6))

for b in range(1, y + 1):
    P *= (b * x ** 2 + 6) / sin(b * x)

k = 1
while k <= c:
    q = 1
    PP = 1
    while q <= d:
        surat = k * q + y * x
        maxraj = sqrt((q * x + y) ** k)
        PP *= surat / maxraj
        q += 1
    SP *= PP
    k += 1

ans = format("{:.2f} {:.2f} {:.2f}".format(S, P, SP))
print(ans)
