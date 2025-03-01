import sys, heapq


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    best[start] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if best[node] < dist:
            continue

        for adj in adj_list[node]:
            if dist + adj[1] < best[adj[0]]:
                best[adj[0]] = dist + adj[1]
                heapq.heappush(pq, (dist + adj[1], adj[0]))


N, M, K = map(int, sys.stdin.readline().split())
A, B = map(int, sys.stdin.readline().split())

adj_list = [[] for _ in range(N+1)]
rate = [0] * (K+1)
for _ in range(M):
    f, t, c = map(int, sys.stdin.readline().split())
    adj_list[f].append([t, c])
    adj_list[t].append([f, c])


for i in range(1, K+1):
    rate[i] = int(sys.stdin.readline())

for i in range(K+1):
    for adj in adj_list:
        if adj:
            for a in adj:
                a[1] += rate[i]

    best = [float('inf')] * (N+1)

    dijkstra(A)
    print(best[B])
