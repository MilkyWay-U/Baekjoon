import sys
input = sys.stdin.readline

n, k = map(int,input().split())
n_list = []
for i in range(n):
    n_list.append(int(input()))
cnt = 0

for i in range(n-1, -1, -1):
    cnt += k // n_list[i]
    k = k % n_list[i]
print(cnt)