from ast import Num
import sys

def Add(N, K, NumList):
    n = 0
    temp = sum(NumList[:K])
    result = temp
    while (n + K < N):
        temp -= NumList[n]
        temp += NumList[n + K]
        if result < temp:
            result = temp
        n += 1
    return result

N, K = map(int,sys.stdin.readline().split())
NumList = list(map(int,sys.stdin.readline().split()))
print(Add(N, K, NumList))