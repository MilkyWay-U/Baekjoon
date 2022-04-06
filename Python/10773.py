import sys
input = sys.stdin.readline
n = int(input())

lst = []
for i in range(n):
    temp = int(input())
    if (temp == 0):
        lst.pop()
    else:
        lst.append(temp)

print(sum(lst))