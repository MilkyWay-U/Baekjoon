from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
lst = deque()

def empty():
    if len(lst) == 0:
        return 1
    else:
        return 0

def size():
    return len(lst)

for _ in range(n):
    a = list(map(str, input().split()))
    if a[0] == "push_front":
        lst.appendleft(int(a[1]))
    elif a[0] == "push_back":
        lst.append(int(a[1]))
    elif a[0] == "pop_front":
        if empty() == 1:
            print(-1)
        else:
            print(lst[0])
            lst.popleft()

    elif a[0] == "pop_back":
        if empty() == 1:
            print(-1)
        else:
            print(lst[-1])
            lst.pop()

    elif a[0] == "size":
        print(size())



    elif a[0] == "empty":
        print(empty())
    
    elif a[0] == "front":
        if empty() == 1: print(-1)
        else: print(lst[0])
    elif a[0] == "back":
        if empty() == 1: print(-1)
        else: print(lst[-1])