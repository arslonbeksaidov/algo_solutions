string_length = int(input())
text = input()
print(text.translate({ord('$'): ""}))
