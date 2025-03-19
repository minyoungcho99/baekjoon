# 특정한 최단경로
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
            if next_dist + dist < best[next_node]:
                best[next_node] = next_dist + dist
                heapq.heappush(pq, (next_dist + dist, next_node))


N, E = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N+1)]
INF = 1e9

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())

v1_v2 = 0
v2_v1 = 0

best = [1e9] * (N+1)
dijkstra(1)
v1_v2 += best[v1]
v2_v1 += best[v2]

best = [1e9] * (N+1)
dijkstra(v1)
v1_v2 += best[v2]
v2_v1 += best[N]

best = [1e9] * (N+1)
dijkstra(v2)
v1_v2 += best[N]
v2_v1 += best[v1]

if v1_v2 >= INF and v2_v1 >= INF:
    print(-1)

else:
    if v1_v2 <= v2_v1:
        print(v1_v2)

    else:
        print(v2_v1)