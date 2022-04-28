N, K = map(int,input().split())
result = 1
if (N - K) < K:
    K = N - K
for i in range(K):
    result *= (N-i)
    
for i in range(1,K+1):
    result = result // i
print(result % 10007)