N = int(input())
M = 0b11111111111111111111111111111111
num = N^M
num = format(num, 'b')
result = format(int(num,2) + 1, 'b')
result_list = list(str(result))
num = '%32s' % str(num)
num_list = list(num.replace(' ','1'))
cnt = 0
for i in range(32):
    if result_list[i] == num_list[i]:
        cnt += 1
print(cnt)
