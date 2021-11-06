from math import *

x, y, c, d = map(int, input().split())

S, P, SP = 0, 0, 0

for i in range(1, x + 1):
    S += (i ** 4 + i ** 2 + 3) / sqrt(i + e ** i)

for k in range(1, y + 1):
    P += (k + 1)  / (k ** 3 + 5 * k)

m = 1
while m <= c:
    n = 1
    PP = 1
    while n <= d:
        surat = abs(m ** n - n ** m)
        maxraj = m ** n + n ** m
        PP *= sqrt(surat / maxraj)
        n += 1
    SP += PP
    m += 1

ans = format("{:.2f} {:.2f} {:.2f}".format(S, P, SP))
print(ans)
