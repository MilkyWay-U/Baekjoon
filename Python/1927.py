import sys, heapq

input = sys.stdin.readline
heap = []
n = int(input())
for _ in range(n):
    m = int(input())
    if m == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, m)