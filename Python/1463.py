N = int(input())
num = 1
cnt = 0
while (N != num):
    if (N >= (num * 3)):
        num *= 3
        cnt += 1
    elif ( N >= (num *2)):
        num *= 2
        cnt += 1
    else:
        num += 1        
        cnt += 1
print(cnt)