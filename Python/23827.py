import sys
num = int(input())
num_list = list(map(int,sys.stdin.readline().split()))
res = 0
sum = sum(num_list)
for i in num_list:
    sum -= i
    res += (i * sum)
res = res % 1000000007
print(res)