import sys

N = int(input())
M = int(input())

num_list = list(map(int,sys.stdin.readline().split()))
num_list.sort()

cnt = 0
start, end = 0, N-1
while start < end:
    if num_list[start] + num_list[end] == M:
        cnt += 1
        start += 1
        end -= 1
    elif num_list[start] + num_list[end] < M:
        start += 1
    else:
        end -= 1

print(cnt)