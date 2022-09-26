"""시간초과

cnt = int(input())
lst = list(map(int,input().split()))
cnt_lst = [0] * cnt
set_lst = sorted(set(lst))


print(*cnt_lst)
"""

import sys
input = sys.stdin.readline
cnt = int(input())


lst = list(map(int,input().split()))
set_lst = list(sorted(set(lst)))
lst_dic = {set_lst[i]:i for i in range(len(set_lst))}

for i in lst:
    print(lst_dic[i], end = ' ')