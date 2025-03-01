import sys, heapq

N, T = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N)]
best = [float('inf')] * N

for _ in range(T):
    a, b, w = map(int, sys.stdin.readline().split())
    adj_list[a].append((b, w))


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
                best[adj[0]] = dist + adj[1]
                heapq.heappush(pq, (dist + adj[1], adj[0]))


dijkstra(0)
if type(best[N-1]) == float:
    print("impossible")
else:

    print(best[N-1])
