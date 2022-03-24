import sys

N, K = map(int,sys.stdin.readline().split())
NumList = list(map(int,sys.stdin.readline().split()))
n = 0
MaxVal = NumList[0] + NumList[K-1]
while (n + K - 1 < N):
    if MaxVal < NumList[n] + NumList[n + K-1]:
        MaxVal = NumList[n] + NumList[n + K-1]
    n += 1
print(MaxVal)