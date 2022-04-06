import sys

m = int(input())
s = []
for _ in range(m):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        s.clear()
        if temp[0] == "all":
            for i in range(1,21):
                s.append(i)
        continue
    a, b = temp[0],temp[1]
    b = int(b)
    if a == "add":
        if b not in s:
            s.append(b)
    elif a == "remove":
        if b in s:
            s.remove(b)
    elif a == "check":
        print(1 if b in s else 0)
    elif a == "toggle":
        if b in s:
            s.remove(b)
        else:
            s.append(b)