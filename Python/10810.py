a, b = map(int,input().split())

lst = [0] * a
for _ in range(b):
    i,j,k = map(int,input().split())
    for x in range(i, j + 1):
        lst[x - 1] = k
for i in range(a):
    print(lst[i], end =' ')     