import sys

lstL = list(sys.stdin.readline().rstrip())
lstR = []

for _ in range(int(sys.stdin.readline())):
    text = list(sys.stdin.readline().split())

    if text[0] == "P":
        lstL.append(text[1])
    elif text[0] == "L":
        if lstL:
            lstR.append(lstL.pop())
    elif text[0] == "D":
        if lstR:
            lstL.append(lstR.pop())
    else:
        if lstL:
            lstL.pop()
    
lstL.extend(reversed(lstR))
print(''.join(lstL))

