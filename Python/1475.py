import sys, math
input = sys.stdin.readline
lst = [0 for _ in range(10)]
n = input().strip()
for i in n:
    i = int(i)
    lst[i] += 1

lst[6] = math.ceil((lst[9] + lst[6]) / 2)
lst[9] = 0
print(max(lst))