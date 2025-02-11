# 트리의 부모 찾기
import sys
from collections import deque

N = int(sys.stdin.readline())

parent = [0] * (N+1)
visited = [False] * (N+1)
adj_list = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def bfs(root):
    visited[root] = True
    q = deque([root])

    while q:
        curr = q.popleft()

        for adj in adj_list[curr]:
            if not visited[adj]:
                visited[adj] = True
                parent[adj] = curr
                q.append(adj)

bfs(1)

for p in parent[2:]:
    print(p)