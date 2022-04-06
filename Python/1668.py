import sys
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

def check(lst):
    max = lst[0]
    cnt = 1

    for i in lst:
        if (max < i):
            max = i
            cnt += 1
    return cnt
print(check(lst))
lst = reversed(lst)
lst = list(lst)
print(check(lst))