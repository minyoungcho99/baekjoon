# 숨바꼭질 3
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [False] * 100001

def bfs(start):
    visited[start] = True
    q = deque([(start, 0)])

    while q:
        node, time = q.popleft()
        if node == K:
            break

        if 0 <= node * 2 <= 100000 and not visited[node * 2]:
            q.append((node * 2, time))
            visited[node * 2] = True

        if 0 <= node - 1 <= 100000 and not visited[node - 1]:
            q.append((node - 1, time + 1))
            visited[node - 1] = True

        if 0 <= node + 1 <= 100000 and not visited[node + 1]:
            q.append((node + 1, time + 1))
            visited[node + 1] = True

    return time

print(bfs(N))