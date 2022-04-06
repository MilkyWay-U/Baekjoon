n = int(input())
lst = []
max = 0
l_cnt = 0
r_cnt = 0
for _ in range(n):
    lst.append(int(input()))

for i in lst:
    if (max < i):
        max = i
        l_cnt += 1
lst = reversed(lst)
lst = list(lst)
max = 0
for i in lst:
    if (max < i):
        max = i
        r_cnt += 1

print(l_cnt)
print(r_cnt)
