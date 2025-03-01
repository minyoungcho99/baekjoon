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


V, E, P = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    adj_list[A].append((B, C))
    adj_list[B].append((A, C))  # 양방향

impossible = False
for _ in range(1):
    expected = 0
    taken = 0

    best = [float('inf')] * (V + 1)

    dijkstra(1)
    if type(best[V]) == float:
        impossible = True
        break

    expected += best[V]

    if type(best[P]) == float:
        impossible = True
        break

    taken += best[P]
    best = [float('inf')] * (V + 1)
    dijkstra(P)
    taken += best[V]

    if expected < taken:
        impossible = True

if impossible:
    print("SORRY")
else:
    print("OKAY")
