words = list(input())
n = 1
for i in range(len(words) // 2):
    if words[0 + i] == words[len(words) - 1 - i]:
        continue
    else:
        print(0)
        n = 0
        break
if n == 1:
    print(1)