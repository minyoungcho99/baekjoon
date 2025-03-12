# 카드 정렬하기
import sys, heapq

T = int(sys.stdin.readline())

for _ in range(T):
    total = 0
    N = int(sys.stdin.readline())
    chs = list(map(int, sys.stdin.readline().split()))

    heapq.heapify(chs)

    while len(chs) > 1:
        mini = heapq.heappop(chs) + heapq.heappop(chs)
        total += mini
        heapq.heappush(chs, mini)

    print(total)