import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def bfs():
    cnt = 0
    visited[1] = True
    q = deque([(1, 0)])

    while q:
        x, depth = q.popleft()
        if depth == 1 or depth == 2:
            cnt += 1

        if depth > 2:
            break

        for adj in adj_list[x]:
            if not visited[adj]:
                visited[adj] = True
                q.append((adj, depth+1))

    return cnt


print(bfs())