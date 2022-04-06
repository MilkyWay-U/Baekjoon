lst = list(map(int,input().split()))
right = [1, 1, 2, 2, 2, 8]
for i in range(6):
    lst[i] = right[i] - lst[i]

print(' '.join(list(map(str,lst))))