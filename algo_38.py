q = input().split()
new_array = []
for x in q:
    if float(x) >= 1 and float(x) <=3:
        new_array.append(x)

print(" ".join(new_array))
