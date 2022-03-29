# (a*b) % c = (a%c) * (b%c) %c
import sys

a, b, c = map(int, sys.stdin.readline().split())

def mul(length):
    if length == 1:
        return a % c
    if length % 2 == 0:
        temp = mul(length // 2)
        return temp * temp % c
    else:
        temp = mul(length // 2)
        return temp * temp * a % c
print(mul(b))