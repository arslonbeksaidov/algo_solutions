from math import *

x, y, c, d = map(int, input().split())

S, P, SP = 0, 1, 0

for n in range(1, x + 1):
    S += 1 / (5 - 17 * n + n ** 3)

for m in range(1, y + 1):
    P *= sqrt(abs(m - 5) + 1) / (m ** 2 + 4 * m - 1)

i = 1
while i <= c:
    k = 1
    PP = 1
    while k <= d:
        surat = (-1) ** i * pow(abs(sin(k) + e ** k), 1 / 7)
        maxraj = 2 * abs(4 * i ** 3 - k ** 4)
        PP *= surat / maxraj
        k += 1
    SP += PP
    i += 1

ans = format("{:.2f} {:.2f} {:.2f}".format(S, P, SP))
print(ans)
