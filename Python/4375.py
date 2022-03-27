def div(num):
    temp = 1
    result = 1
    while (temp % num != 0):
        result += 1
        temp = temp * 10 + 1
    return result

if __name__ == "__main__":
    while True:
        try:
            print(div(int(input())))
        except EOFError:
            break