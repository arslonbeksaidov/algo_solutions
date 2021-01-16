import math


def repeater(radius):
    p = math.pi
    return "{:.2f}".format(p * radius ** 2)


def algo_2():
    r1 = input().split(' ')
    ans = ''
    for x in r1:
        ans += repeater(int(x)) + ' '
    print(ans)


algo_2()

# print(" ".join(["{:.2f}".format(r ** 2 * 3.1415926) for r in map(int, input().split())]))
