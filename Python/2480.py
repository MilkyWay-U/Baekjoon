a, b, c = map(int,input().split())

while True:
    if a == b and b == c and c == a:
        print(10000 + (a * 1000))
        break
    if a == b:
        print(1000 + (a * 100))
        break
    elif b == c:
        print(1000 + (b * 100))
        break
    elif a == c:
        print(1000 + (a * 100))
        break
    else:
        max_num = max(a,b,c)
        print(max_num * 100)
        break