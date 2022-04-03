N = int(input())
num = 1
cnt = 0
while (N != num):
    while (N >= (num * 3)):
        num *= 3
        cnt += 1
    while ( N >= (num *2)):
        num *= 2
        cnt += 1
    while ( N >= (num+1)):
        num += 1        
        cnt += 1
print(cnt)