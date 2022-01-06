a, b = map(int,input().split())

#최대 공약수 구하는 함수
def gcd(a, b):
    while b > 0:
        a ,b = b, a % b
    return a

# 최소 공배수 구하는 함수
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a,b))
print(lcm(a,b))