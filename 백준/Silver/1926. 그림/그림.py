# 그림
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = []
visited = [[False] * M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs(sx, sy):
    area = 1
    visited[sx][sy] = True
    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == 1:
                area += 1
                q.append((nx, ny))
                visited[nx][ny] = True

    return area

num = 0
max_area = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j] == 1:
            num += 1
            max_area = max(max_area, bfs(i, j))

print(num)
print(max_area)