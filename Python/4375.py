def div(num):
    temp = 1
    result = 1
    while temp % num != 0:
        temp *= 10
        temp += 1
        result +=1
    return result

print(div(int(input())))