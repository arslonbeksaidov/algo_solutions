z = input()
array = list(map(int, input().split()))

i = 1
s = 0
p = 1
while i < len(array) + 1:
    if i % 2 != 0:
        p *= array[i - 1]
    else:
        s += array[i - 1]
    i += 1
print("{:.2f}".format(p / s))
