satr = input().split()
ans = []
for x in satr:
    if "Info" in x:
        ans.append(x)

print(" ".join(ans))
