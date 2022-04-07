import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
lst.sort(reverse=True)
sum = 0
for i in range(1, n + 1):
    sum += (lst[i-1] * i)
print(sum)