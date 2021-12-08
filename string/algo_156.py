n = input().split()
i, j = map(int, input().split())

n[i - 1], n[j - 1] = n[j - 1], n[i - 1]
print(" ".join(n))
