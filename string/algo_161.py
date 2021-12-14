string_length = int(input())
text = input()

A, S, L, O, M = 2, 2, 1, 1, 1

for x in text:
    if x == "A":
        A -= 1
    if x == "S":
        S -= 1
    if x == "L":
        L -= 1
    if x == "O":
        O -= 1
    if x == "M":
        M -= 1
ans = [A, S, L, O, M]

for i in ans:
    if i > 0:
        print("NO")
        break
else:
    print('YES')
