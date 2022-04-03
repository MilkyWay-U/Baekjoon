N = int(input())
lst = []
for _ in range(N):
    lst.append(input().split())
lst.sort(key = lambda x : int(x[0]))
for i in range(N):
    print(lst[i][0], lst[i][1])