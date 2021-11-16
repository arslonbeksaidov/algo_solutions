z = input()
array = list(map(int, input().split()))
value = int(input())
i = 0
s = 0
while i < len(array):
    if array[i] > value:
        s += array[i]
    i += 1
print(s)
