
import sys
sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())
pattern = input()
cnt = 0
for i in pattern:
    if i != '*':
        cnt += 1
    else:
        break
first = []
for i in range(cnt):
    first.append(pattern[i])
cnt = 0
for i in range(len(pattern)-1, 0, -1):
    if pattern[i] != '*':
        cnt +=1
    else:
        break
end = []
for i in range(cnt):
    end.append(pattern[len(pattern)-1 -i])
for i in range(N):
    a = sys.stdin.readline()
    result = 1
    for i in range(len(first)):
        if a[i] != first[i]:
            result = 0
    if result == 1:
        for i in range(len(end)):
            if a[len(a)-2-i] != end[i]:
                result = 0

    if result == 1:
        print("DA")
    else:
        print("NE")