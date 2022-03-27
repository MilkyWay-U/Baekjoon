def div(num):
    temp = '1'
    result = 1
    while True:
        if int(temp) % num == 0:
            result = len(temp)
            break
        temp += '1'
    return result

print(div(int(input())))