def factor(a,b):
    if b % a == 0:
        return 1
    return 0
def multiple(a, b):
    if a % b == 0:
        return 1
    return 0

while True:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        break
    if factor(a,b) == 1:
        print("factor")
    elif multiple(a,b) == 1:
        print("multiple")
    else:
        print("neither")
