# 카드 합체 놀이
import sys, heapq

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

heapq.heapify(card)

for _ in range(M):
    x, y = heapq.heappop(card), heapq.heappop(card)

    heapq.heappush(card, x+y)
    heapq.heappush(card, x+y)

print(sum(card))