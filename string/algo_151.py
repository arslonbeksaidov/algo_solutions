satr = input()
cnt = 0
for x in satr:
    if x in ['A', 'a', 'O', 'o', 'I', 'i', 'U', 'u', 'E', 'e']:
        cnt += 1

print(cnt)
