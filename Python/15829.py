from re import L
import sys
input = sys.stdin.readline
n = int(input())
lst = input().strip()
ord_lst = []
for i in lst:
    ord_lst.append(ord(i)- 96)
result = 0
for i in range(n):
    result += (ord_lst[i] * (31 ** i))
result %= 1234567891
print(result)