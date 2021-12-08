satr = input().split()
ans = []
cnt = 0
for x in satr:
    if x[-1] == "A" and x[-2] == "N":
        ans.append(x)
        cnt += 1

print(cnt)
print(" ".join(ans))
