satr = list(input())
ans = ''
open_close = 'close'
part_string = ''
for x in satr:
    if x == "(":
        open_close = "open"
        continue
    if x == ")":
        open_close = "close"
        ans += part_string[::-1]
        part_string = ''
        continue
    if open_close == "open":
        part_string += x
    elif open_close == "close":
        ans += x

print(ans)
