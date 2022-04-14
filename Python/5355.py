import sys
input = sys.stdin.readline
def mul(num):
    return num * 3
def sum(sum):
    return num + 5
def sub(sum):
    return num - 7
n = int(input())
for _ in range(n):
    lst = list(map(str,input().strip().split()))
    num = float(lst[0])
    lst.remove(lst[0])
    for i in lst:
        if i == "@":
            num = mul(num)
        elif i == "%":
            num = sum(num)
        else:
            num = sub(num)
    print("{:0.2f}".format(num))
        
