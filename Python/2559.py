import sys

def Add(N, K, NumList):
    temp = sum(NumList[:K])
    result = temp
    for i in range(K, N):
        temp += NumList[i]
        temp -= NumList[i - K]
        if result < temp:
            result = temp
    return result

N, K = map(int,sys.stdin.readline().split())
NumList = list(map(int,sys.stdin.readline().split()))
print(Add(N, K, NumList))