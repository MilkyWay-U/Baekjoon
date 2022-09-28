arr = []
for i in range(9):
    arr.append(int(input()))
for i in range(8):
    for j in range(i + 1, 9):
        if (sum(arr) - arr[i] - arr[j] == 100):
            x, y = arr[i], arr[j]
            break
arr.remove(x)
arr.remove(y)
for i in arr:
    print(i)
