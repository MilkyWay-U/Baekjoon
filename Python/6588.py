import sys

num = 1000001
arr = [True for _ in range(num)]

for i in range(2, 1001):
    if arr[i]:
        for j in range(2*i,num, i):
            arr[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    flag = 0
    
    for k in range(3, n):
        if arr[k] and arr[n-k]:
            print(str(n)+" = "+str(k)+" + "+str(n-k))
            flag = 1
            break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")
    