# 최소비용 구하기
import sys, heapq


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    best[start] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if best[node] < dist:
            continue

        for next_node, next_dist in adj_list[node]:
            if dist + next_dist < best[next_node]:
                best[next_node] = dist + next_dist
                heapq.heappush(pq, (dist+next_dist, next_node))


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj_list =[[] for _ in range(N+1)]
best = [float('inf')] * (N+1)

for _ in range(M):
    A, B, V = map(int, sys.stdin.readline().split())
    adj_list[A].append((B, V))

A, B = map(int, sys.stdin.readline().split())
dijkstra(A)
print(best[B])