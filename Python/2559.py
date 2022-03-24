import sys

N, K = map(int,sys.stdin.readline().split())
NumList = list(map(int,sys.stdin.readline().split()))
n = 0
AddVal = 0
for i in range(K):
    AddVal += NumList[n+i]
MaxVal = AddVal
while (n + K < N):
    AddVal -= NumList[n]
    AddVal += NumList[n + K]
    if MaxVal < AddVal:
        MaxVal = AddVal
    n += 1
print(MaxVal)