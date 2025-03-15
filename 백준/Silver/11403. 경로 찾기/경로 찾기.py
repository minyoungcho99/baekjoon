# 경로 찾기
import sys
from collections import deque


def bfs(start, adj):
    visited = [[False] * N for _ in range(N)]
    ans[start][adj] = 1
    visited[start][adj] = True
    q = deque([adj])

    while q:
        x = q.popleft()

        for i in range(N):
            if adj_matrix[x][i] == 1 and not visited[x][i]:
                visited[x][i] = True
                ans[start][i] = 1
                q.append(i)


def traversal():
    for i in range(N):
        for j in range(N):
            if adj_matrix[i][j] == 1:
                bfs(i, j)


N = int(sys.stdin.readline())

adj_matrix = []
ans = [[0] * N for _ in range(N)]

for _ in range(N):
    adj_matrix.append(list(map(int, sys.stdin.readline().split())))

traversal()
for a in ans:
    print(" ".join(map(str, a)))