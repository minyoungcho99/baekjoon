# 연결 요소의 개수
import sys
from collections import deque

N, M = map(int ,sys.stdin.readline().split())

ans = 0
visited = [False] * (N+1)
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int ,sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def bfs(node):
    visited[node] = True
    q = deque([node])

    while q:
        popped = q.popleft()
        for adj_node in adj_list[popped]:
            if not visited[adj_node]:
                visited[adj_node] = True
                q.append(adj_node)


for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        ans += 1

print(ans)