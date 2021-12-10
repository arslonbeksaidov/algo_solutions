string = input().split()
i = 0
cnt = 0
while i < len(string):
    if string[i][0] == "a" and string[i][-1] == "b":
        cnt += 1
    i += 1
print(cnt)
