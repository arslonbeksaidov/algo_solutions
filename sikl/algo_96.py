from math import *

x, y, c, d = map(int, input().split())

S, P, SP = 0, 1, 1

for k in range(1, x + 1):
    S += (-1) ** k * (k + 1) / (k ** 3 + k ** 2 + 1)

for i in range(1, y + 1):
    P *= (i ** 3 + abs(i - 9)) / (log(i) + 7 * i)

n = 1
while n <= c:
    m = 1
    PP = 0
    while m <= d:
        surat = (-1) ** m * log(m + 5)
        maxraj = m ** (n + 3) + n * m
        PP += surat / maxraj
        m += 1
    SP *= PP
    n += 1

ans = format("{:.2f} {:.2f} {:.2f}".format(S, P, SP))
print(ans)
