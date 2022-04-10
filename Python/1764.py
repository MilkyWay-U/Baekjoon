#시간초과뜸... ㅜㅠㅜ

import sys
input = sys.stdin.readline
lst = []
check_lst = []
n, m = map(int,input().split())
for _ in range(n):
    lst.append(input().strip())
for _ in range(m):
    name = input().strip()
    if name in lst:
        check_lst.append(name)
     
print(len(check_lst))
for i in check_lst:
    print(i)