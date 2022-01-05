N = int(input())

N_list = []

while N > 0:
    i = 0
    N_list.append(N % (10**(i + 1)))
    N = N // (10**(i + 1))
    i += 1
N_list.sort()
N_list.reverse()
for i in N_list:
    print(i,end="")
