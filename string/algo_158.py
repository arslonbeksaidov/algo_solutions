string = input().split()
i = 0
odd = 0
even = 0
while i < len(string):
    if len(string[i]) % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1
print(odd * even)
