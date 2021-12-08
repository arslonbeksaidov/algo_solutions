n = input().split()
cnt = 0
ans = [cnt + 1 for x in n if "A" <= x[0] <= "Z"]
print(sum(ans))
