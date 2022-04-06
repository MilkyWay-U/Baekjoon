import sys
input = sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
    temp = input().strip().split()
    if len(temp) == 1:
        if temp[0] == "all":
            s = set([i for i in range(1,21)])
        else:
            s = set()
        continue

    a, b = temp[0],temp[1]
    b = int(b)
    if a == "add":
        if b not in s:
            s.add(b)
    elif a == "remove":
        if b in s:
            s.discard(b)
    elif a == "check":
        print(1 if b in s else 0)
    elif a == "toggle":
        if b in s:
            s.discard(b)
        else:
            s.add(b)