import sys
input = sys.stdin.readline
n = int(input())
n_lst = list(map(int,input().split()))
m = int(input())
m_lst = list(map(int,input().split()))
cnt_lst = [0] * len(m_lst)
for i in range(len(m_lst)):
    for j in n_lst:
        if m_lst[i] == j:
            cnt_lst[i] += 1
            break
print(*cnt_lst)