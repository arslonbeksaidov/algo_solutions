string = input()
i = 0
ans = ''
while i < len(string):
    if string[i].islower():
        ans += string[i].upper()
    else:
        ans += string[i].lower()
    i += 1
print(ans)
