def check(a, temp):
    for i in range(temp // 2 + 1):
        if (a[i] != a[temp - i]):
            return False
    return True

import sys
input = sys.stdin.readline
a = int(input())
while (a != 0):
    a = str(a)
    temp = len(a) - 1
    if check(a, temp):
        print("yes")
    else:
        print("no")
    a = int(input())