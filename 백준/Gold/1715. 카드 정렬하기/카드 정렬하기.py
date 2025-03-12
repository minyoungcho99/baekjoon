# 카드 정렬하기
import sys, heapq


def sort_card(c):
    total = 0
    heapq.heapify(c)

    while len(c) > 1:
        min_sum = heapq.heappop(c) + heapq.heappop(c)
        total += min_sum
        heapq.heappush(c, min_sum)

    print(total)


N = int(sys.stdin.readline())
card = []

for _ in range(N):
    card.append(int(sys.stdin.readline()))

sort_card(card)