# 가장 먼 곳
import sys, heapq

def dijkstra(start, b):
    pq = []
    heapq.heappush(pq, (0, start))
    best[b][start] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if best[b][node] < dist:
            continue

        for cand, c_dist in adj_list[node]:
            cand_dist = dist + c_dist
            if cand_dist < best[b][cand]:
                best[b][cand] = cand_dist
                heapq.heappush(pq, (cand_dist, cand))

N = int(sys.stdin.readline())
adj_list = [[] for _ in range(N+1)]
fr = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))

best = [[float('inf')] * (N+1) for _ in range(3)]

dijkstra(fr[0], 0)
dijkstra(fr[1], 1)
dijkstra(fr[2], 2)

max_dist = 0
max_i = 0

for i in range(1, N+1):
    dist = min(best[0][i], best[1][i], best[2][i])
    
    if dist > max_dist:
        max_dist = dist
        max_i = i
    
print(max_i)