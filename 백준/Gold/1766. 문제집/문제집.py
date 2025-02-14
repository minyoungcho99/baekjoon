# 문제집
import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
ans = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

q = []
heapq.heapify(q)

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    x = heapq.heappop(q)
    ans.append(x)

    for adj in graph[x]:
        indegree[adj] -= 1
        if indegree[adj] == 0:
            heapq.heappush(q, adj)

print(" ".join(map(str, ans)))