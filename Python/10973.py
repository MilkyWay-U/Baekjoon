import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

for i in range(n-1 ,0 , -1):
    if lst[i-1] > lst[i]:
        for j in range(n-1, 0, -1):
            if lst[i - 1] > lst[j]:
                lst[i-1],lst[j] = lst[j],lst[i-1]
                lst = lst[:i] + sorted(lst[i:])
                print(*lst)
                exit()

print(-1)