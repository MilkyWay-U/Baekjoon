import sys
input = sys.stdin.readline

num = int(input())
N_List = []

for i in range(num):
    x,y = map(int,input().split())
    N_List.append([y,x])

sort_list = sorted(N_List)
for y,x in sort_list:
    print(x,y)