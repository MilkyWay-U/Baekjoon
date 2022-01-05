pibo_num = [0] * 91
# 한번 계산된 결과를 메모이제이션하기 위한 리스트

def pibo(n):
    if n <= 1:
        return n
    
    if pibo_num[n] != 0:
        return pibo_num[n]
        # 한번 계산했던 건 그대로 반환

    pibo_num[n] = pibo(n - 1) + pibo (n - 2)
    return pibo_num[n]

n = int(input())
print(pibo(n))