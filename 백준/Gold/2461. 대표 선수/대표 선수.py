# 대표 선수
import sys, heapq

N, M = map(int, sys.stdin.readline().split())
ptr = [0] * N
player = []

for _ in range(N):
    player.append(sorted(list(map(int, sys.stdin.readline().split()))))

pq = []
min_diff = float('inf')
max_val = 0

for idx in range(N):
    heapq.heappush(pq, (player[idx][0], idx, 0))
    max_val = max(max_val, player[idx][0])

while pq:
    min_val, min_idx, min_pointer = heapq.heappop(pq)
    min_diff = min(min_diff, max_val - min_val)

    if min_pointer == M - 1:
        break

    heapq.heappush(pq, (player[min_idx][min_pointer+1], min_idx, min_pointer+1))
    max_val = max(max_val, player[min_idx][min_pointer+1])

print(min_diff)