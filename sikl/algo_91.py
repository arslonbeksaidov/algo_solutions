import math

a, b, c, d = map(int, input().split())

S, P, SP = 0, 1, 0

for m in range(1, a + 1):
    S += (3 * m ** 3 + 4 * m + 5) / (m ** 3 + math.log(m))

for k in range(1, b + 1):
    P *= k / (k ** 3 + 7 * k + 5)

i = 1
while i <= c:
    m = 1
    PP = 1
    while m <= d:
        PP *= (math.log(i) + m ** i) / (m ** i)
        m += 1
    SP += PP
    i += 1

ans = format("{:.2f} {:.2f} {:.2f}".format(S, P, SP))
print(ans)
