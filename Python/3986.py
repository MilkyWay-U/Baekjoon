import sys
input = sys.stdin.readline
num = int(input())
 # 아직 다 못품;;; 킹받네;;;
cnt = 0
for i in range(num):
    word = input().rstrip()
    word_stack = []]
    for j in range(len(word)):
        if word_stack and word[j] == word_stack[-1]:
            word_stack.pop()
        else:
            word_stack.append(word[j])
    
    if not word_stack:
        cnt += 1
print(cnt)

