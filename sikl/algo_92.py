import math

x, y, a, b = map(int, input().split())

S, P, SP = 0, 1, 0

for f in range(1, x + 1):
    S += (f ** 2 + 2 * f) / (f ** 3 + f * math.cos(f) ** 2 + 1)

for i in range(1, y + 1):
    P *= (i ** 2 + 1) / (math.pow(i, 3 / i) + 2)

i = 1
while i <= a:
    k = 1
    PP = 1
    while k <= b:
        surat = (k ** i + k ** (1 / i))
        maxraj = (k ** 3 + i ** (1 / k))
        PP *= math.log((surat / maxraj))
        k += 1
    SP += PP
    i += 1

ans = format("{:.2f} {:.2f} {:.2f}".format(S, P, SP))
print(ans)
