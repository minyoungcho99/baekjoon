import sys
import heapq


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    best[start] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if best[node] < dist:
            continue

        for next_node, next_dist in adj_list[node]:
            new_dist = dist + next_dist
            if new_dist < best[next_node]:
                best[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
                trace[next_node] = node 


def get_path(end):
    path = []
    while end:
        path.append(end)
        end = trace[end]
    return path[::-1]  


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj_list = [[] for _ in range(N + 1)]
best = [float('inf')] * (N + 1)
trace = [0] * (N + 1) 

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    adj_list[a].append((b, c))

A, B = map(int, sys.stdin.readline().split())
dijkstra(A)

print(best[B])
path = get_path(B)
print(len(path))
print(" ".join(map(str, path)))