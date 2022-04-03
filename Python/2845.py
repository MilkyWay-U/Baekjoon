import sys
input = sys.stdin.readline
L, P = map(int,input().split())
lst = list(map(int,input().split()))

sum = L * P
print((lst[0] - sum), (lst[1] - sum),(lst[2] - sum),(lst[3] - sum),(lst[4] - sum))