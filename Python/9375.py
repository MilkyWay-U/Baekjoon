from collections import Counter

n = int(input())
for i in range(n):
    m = int(input())
    wear = []
    for j in range(m):
        a, b = input().split()
        wear.append(b)
    num = 1
    wear_count = Counter(wear)
    for k in wear_count:
        num *= wear_count[k] + 1
    print(num - 1)