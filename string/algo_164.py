text = input()

start, end = map(int, input().split())

if start < end:
    print(text[start - 1:end])
else:
    new_text = ''
    i = len(text) - 1
    while i >= 0:
        if start >= i + 1 >= end:
            new_text = new_text + text[i]
        i -= 1
    print(new_text)
