import sys
input = sys.stdin.readline
def solve(temp, N_list, a):
    for i in N_list:
        if temp != i % a:
            return 1
    return 0

N = int(input())
N_list = []
for _ in range(N):
    N_list.append(int(input()))
result = []
for i in range(2,int(max(N_list)**(1/2))+2):
    temp = N_list[0] % i
    if solve(temp,N_list, i) == 0:
        result.append(i)
for k in result:
    print(k, end = ' ')