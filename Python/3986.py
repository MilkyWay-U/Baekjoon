import sys
input = sys.stdin.readline

n = int(input())
result = 0

for i in range(n):
    s = input().strip()
    s_stack = []
    for j in s:
        if s_stack and s_stack[-1] == j:
                s_stack.pop()
        else:
            s_stack.append(j)
    if not s_stack:
        result += 1
print(result)