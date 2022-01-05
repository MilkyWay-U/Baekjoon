import sys
N = int(sys.stdin.readline())
N_list = []
for i in range(N):
    N_list.append(list(map(int,sys.stdin.readline().split())))

N_list = sorted(N_list, key = lambda x: (x[1], x[0]))
# x[0] -> 시간하는 시간을 기준으로 오름차순
# x[1] -> 끝나는 시간을 기준으로 다시 오름차순
end = 0
cnt = 0

for i, j in N_list:
    if i >= end:
        cnt += 1
        end = j
print(cnt)

