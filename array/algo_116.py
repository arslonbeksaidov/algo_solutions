
z = input()
array = list(map(float, input().split()))
maxx = max(array)
new_list = " ".join(map(lambda x: "{:.2f}".format(x / maxx), array))
print(new_list)
