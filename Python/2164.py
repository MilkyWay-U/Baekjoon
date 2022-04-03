N = int(input())

temp = 2

while True:
    if (N == 1 or N == 2):
        print(N)
        break
    temp *= 2
    if (temp >= N):
        print((N - (temp // 2)) * 2)
        break