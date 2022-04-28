N = int(input())
lst = list(map(int,input().split()))
result = []
first = lst[0]
del(lst[0])
def gcd(a, b):
    num = b
    div = a
    rest = num % div
    while rest != 0:
        num = div
        div = rest
        rest = num % div
    return div
for i in lst:
    if first % i == 0:
        print(str(first//i)+"/1")
    else:
        temp = gcd(first,i)
        print(str(first//temp)+"/"+str(i//temp))