import sys

N, K = map(int,sys.stdin.readline().split())
NumList = list(map(int,sys.stdin.readline().split()))
n = 0
MaxVal = NumList[0] + NumList[K-1]
print(MaxVal)

while (n + K - 1 < N):
    AddVal = 0
    for i in range(K):
        AddVal += NumList[n+i]
    if MaxVal < AddVal:
        MaxVal = AddVal
    n += 1
print(MaxVal)