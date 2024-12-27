# 숨바꼭질 2
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [False] * 100001


def in_range(x):
    return 0 <= x < 100001


def bfs(start):
    n = 0
    visited[start] = True
    q = deque([start])

    while q:
        x = q.popleft()

        if x == K:
            n += 1
            continue

        for nx in (2*x, x-1, x+1):
            if in_range(nx) and (not visited[nx] or visited[nx] == visited[x] + 1):
                q.append(nx)
                visited[nx] = visited[x] + 1

    return n


n = bfs(N)

print(visited[K] - 1)
print(n)