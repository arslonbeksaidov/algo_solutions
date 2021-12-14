text = input().split()

max_word_index = 0
max_word_count = 0

i = 0
while i < len(text):
    if len(text[i]) > max_word_count:
        max_word_count, max_word_index = len(text[i]), i
    i += 1
print(text[max_word_index])
