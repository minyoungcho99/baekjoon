# 음악프로그램
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
indeg = [0] * (N+1)
result = []
graph = [[] for _ in range(N+1)]

for _ in range(M):
    temp = list( map(int, sys.stdin.readline().split()))
    num = temp[0]
    for start in range(1, num):
        graph[temp[start]].append(temp[start+1])
        indeg[temp[start+1]] += 1

q = deque([])

for i in range(1, N+1):
    if indeg[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    result.append(x)

    for adj in graph[x]:
        indeg[adj] -= 1
        if indeg[adj] == 0:
            q.append(adj)

if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)