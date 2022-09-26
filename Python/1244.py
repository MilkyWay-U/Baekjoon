def s2(lst, n, j, lst_len):
    if ((n - j) >= 0 and (n + j) < lst_len):
        if (lst[n - j] == lst[n + j]):
            s2(lst, n , j + 1, lst_len)
        return (j + 1)
    return (j - 1)

num = int(input())
lst = list(map(int, input().split()))
cnt = int(input())
lst_len = len(lst)
for i in range(cnt):
    s, n = map(int,input().split())
    n -= 1

    if s == 1:
        while (n < lst_len):
            if lst[n] == 1:
                lst[n] = 0
            else:
                lst[n] = 1
            n += (n + 1)
    else:
        j = s2(lst, n, 1, lst_len)
        if n + j + 1 >= lst_len:
            n += 1
        for i in range(n - j, n + j + 1):
            if i >= lst_len:
                break
            if lst[i] == 1:
                lst[i] = 0
            else:
                lst[i] = 1
    print(*lst)