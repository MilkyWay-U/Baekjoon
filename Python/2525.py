h, m = map(int,input().split())
sum = int(input())

h += sum // 60
m += sum % 60

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24


print(h,m)