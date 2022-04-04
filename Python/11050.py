n, k = map(int,input().split())
sum = 1
for i in range(n - k + 1, n + 1):
    sum *= i
for j in range(1, k + 1):
    sum /= j
print(int(sum))