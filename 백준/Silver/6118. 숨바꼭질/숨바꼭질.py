# 숨바꼭질
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

adj_list = [[] for _ in range(N+1)]  # 1based idx
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def bfs(node):
    visited[node] = True
    q = deque([(node, 0)])

    while q:
        x, dist = q.popleft()
        for adj in adj_list[x]:
            if not visited[adj]:
                visited[adj] = True
                q.append((adj, dist + 1))

    return dist


def find_dist(node, max_dist):
    temp = []
    visited[node] = True
    q = deque([(node, 0)])

    while q:
        x, dist = q.popleft()
        if dist == max_dist:
            temp.append(x)

        for adj in adj_list[x]:
            if not visited[adj]:
                visited[adj] = True
                q.append((adj, dist + 1))

    return temp


max_dist = bfs(1)
visited = [False] * (N+1)
dists = sorted(find_dist(1, max_dist))

ans = [dists[0], max_dist, len(dists)]

print(" ".join(map(str, ans)))