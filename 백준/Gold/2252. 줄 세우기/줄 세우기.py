# 줄 세우기
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
indeg = [0] * (N+1)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    indeg[B] += 1

q = deque([])

for i in range(1, N+1):
    if indeg[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    print(x, end=' ')

    for adj in graph[x]:
        indeg[adj] -= 1
        if indeg[adj] == 0:
            q.append(adj)