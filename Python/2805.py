import sys

N, M = map(int,input().split())

N_list = list(map(int,sys.stdin.readline().split()))

# 이분 탐색 사용
start, end = 0, max(N_list)
while start <= end:
    mid = (start+end) // 2
    sum = 0
    for i in N_list:
        if i > mid:
            sum += (i - mid)
            if sum > M:
                break
    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)