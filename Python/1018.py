import sys
input = sys.stdin.readline

N, M = map(int,input().split())
lst = []
cnt = []

for _ in range(N):
    lst.append(input())

for a in range(N - 7):
    for b in range(M - 7):
        W_1st = 0
        B_1st = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i+j) % 2 == 0:
                    if lst[i][j] == 'W': W_1st += 1
                    if lst[i][j] == 'B': B_1st += 1
                else:
                    if lst[i][j] == 'B': W_1st += 1
                    if lst[i][j] == 'W': B_1st += 1
        cnt.append(W_1st)
        cnt.append(B_1st)
print(min(cnt))