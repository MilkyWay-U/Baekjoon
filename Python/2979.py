a, b, c = map(int,input().split())
N_list = []
for i in range(3):
    N_list.append(list(map(int,input().split())))
min_value = 0
max_value = 0
for i in range(3):
    min_value = min(min_value, N_list[i][0])
    max_value = max(max_value, N_list[i][1])
N_list_len = max_value - min_value
clock = [0] * N_list_len
for i,j in N_list:
    for k in range(i -min_value, j - min_value):
        clock[k] += 1
pay_sum = 0
pay_sum += clock.count(1) * a
pay_sum += clock.count(2) * b * 2
pay_sum += clock.count(3) * c * 3
print(pay_sum)