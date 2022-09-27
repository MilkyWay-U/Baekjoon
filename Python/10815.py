import sys
input = sys.stdin.readline
n = int(input())
n_lst = list(map(int,input().split()))
m = int(input())
m_lst = list(map(int,input().split()))

n_lst.sort()

def bin(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(m):
    if bin(n_lst, m_lst[i], 0, n -1) is not None:
        print(1, end = ' ')
    else:
        print(0, end = ' ')