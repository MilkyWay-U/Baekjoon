n, l = map(int,input().split())
l = str(l)
cnt = 0
result = 0

while cnt != n:
    result += 1
    if l in str(result):
        continue
    cnt += 1
print(result)