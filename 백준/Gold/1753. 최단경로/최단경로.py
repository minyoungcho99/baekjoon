# 최단경로
import sys, heapq


def dijkstra(sx):
    pq = []
    heapq.heappush(pq, (0, sx))
    best[sx] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if best[node] < dist:
            continue

        for adj in adj_list[node]:
            if dist + adj[1] < best[adj[0]]:
                heapq.heappush(pq, (dist + adj[1], adj[0]))
                best[adj[0]] = dist + adj[1]


V, E = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(V + 1)]

best = [float('inf')] * (V + 1)

K = int(sys.stdin.readline())

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adj_list[u].append((v, w))

dijkstra(K)
for idx in range(1, V+1):
    if type(best[idx]) == float:
        print("INF")
    else:
        print(best[idx])