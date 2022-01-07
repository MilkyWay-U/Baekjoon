T = int(input())
for i in range(T):
    x, y =map(int,input().split())
    distance = y - x
    cnt = 0
    move = 1  # cnt 별 이동한 거리
    move_sum = 0   # 이동한 거리의 합

    while move_sum < distance:
        cnt += 1
        move_sum += move  # cnt 수에 해당하는 move를 더함
        if cnt % 2 == 0:
            move += 1
    print(cnt)