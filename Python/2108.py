import sys
from collections import Counter
# 컨테이너에 동일한 값의 자료가 몇 개인지 파악하는데 사용하는 객체
N = int(sys.stdin.readline())
N_list = []
sum = 0
for i in range(N):
    N_list.append(int(sys.stdin.readline()))
    sum += N_list[i]
print(round(sum / N))
# 산술 평균
N_list.sort()
print(N_list[N // 2])
# 중앙값

cnt = Counter(N_list).most_common(2)
# 빈도수가 높은 숫자 2개 가져옴
if len(N_list) > 1:
    if cnt[0][1] == cnt[1][1]:
        # Counter의 결과값은 딕셔너리기 때문에 2차원 리스트 씀
        #[i][0]은 자료의 값
        #[i][1]은 동일한 값의 자료가 몇 개인지
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(max(N_list)- min(N_list))
# 범위

