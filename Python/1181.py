import sys
input = sys.stdin.readline

num = int(input())
N_list = []
for i in range(num):
    N_list.append(input().strip())
set_lst = set(N_list)
N_list = list(set_lst)
N_list.sort()
N_list.sort(key = len)

for i in N_list:
    print(i)


    