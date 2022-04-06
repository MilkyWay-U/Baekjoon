n = int(input())

sum = 1
for i in range(1,n+1):
    sum *= i

result = 0
while (sum % 10 == 0):
    result += 1
    sum /= 10
print(result)