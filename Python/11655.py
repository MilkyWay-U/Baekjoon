def rot13(s_ord):
    for i in range(len(s_ord)):
        if (78> s_ord[i] >= 65 or 110 > s_ord[i] >=97):
            s_ord[i] += 13
        elif (78<= s_ord[i]<= 90) or (110 <= s_ord[i] <= 122):
            s_ord[i] -= 13
    return s_ord

import sys
S = list(sys.stdin.readline())
S_ord = []
for i in S:
    S_ord.append(ord(i))
S_ord = rot13(S_ord)
for i in range(len(S)):
    S[i] = chr(S_ord[i])
    print(S[i],end="")

# N + 13 ==> A
# N => 78
# M + 13 ==> Z
# A => 65
# a => 97
# Z => 90
# z => 122
# chr(ord("B") + 13) => "O"
