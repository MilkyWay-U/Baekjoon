def size_zero(a, N_list):
    if (a[0] != 'size' and a[0] != 'empty'):
        return -1
    if a[0] == 'empty':
        return 1
    else:
        return (0)

import sys
N = int(sys.stdin.readline())
N_list = []
for i in range(N):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push':
        N_list.append(a[1])
    elif len(N_list) == 0:
        print(size_zero(a,N_list))
    elif a[0] == 'pop' or a[0] == 'front':
        print(N_list[0])
        if a[0] == 'pop':
            del(N_list[0])
    elif a[0] == 'size':
        print(len(N_list))
    elif a[0] == 'empty':
        print(0)
    elif a[0] == 'back':
        print(N_list[len(N_list) - 1])
