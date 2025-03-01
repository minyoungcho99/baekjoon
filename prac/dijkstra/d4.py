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
                heapq.heappush(pq, (dist + next_dist, next_node))


N, M, P = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    adj_list[a].append((b, t))


ans = [0] * (N + 1)
for i in range(1, N + 1):
    best = [float('inf')] * (N + 1)
    dijkstra(i)
    ans[i] += best[P]

best = [float('inf')] * (N + 1)
dijkstra(P)

for i in range(1, N + 1):
    ans[i] += best[i]

print(max(ans))
