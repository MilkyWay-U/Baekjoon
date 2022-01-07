import sys

N = int(sys.stdin.readline())
pattern = input().split('*')
front = pattern[0]
back = pattern[1]
for i in range(N):
    a = input()
    if a[:len(front)] == front and a[-len(back):] == back and len("".join(pattern)) <= len(a):
        print("DA")
    else:
        print("NE")
