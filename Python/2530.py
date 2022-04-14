h, m, s = map(int,input().split())
a = int(input())

s += a % 60
a = a// 60
if s > 59:
    s -= 60
    m += 1
m += a % 60
a = a // 60
if m > 59:
    m -= 60
    h += 1
h += a % 24
if h > 23:
    h -= 24
print(h,m,s)