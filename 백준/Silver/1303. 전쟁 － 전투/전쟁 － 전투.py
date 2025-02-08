# 전쟁 - 전투
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = []
pow = [0, 0]
visited = [[False] * N for _ in range(M)]

for _ in range(M):
    board.append(list(sys.stdin.readline().rstrip()))


def in_range(x, y):
    return 0 <= x < M and 0 <= y < N


def bfs(sx, sy, color):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    area = 1
    visited[sx][sy] = True
    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == color:
                q.append((nx, ny))
                visited[nx][ny] = True
                area += 1

    return area


for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if board[i][j] == 'W':
                pow[0] += bfs(i, j, 'W') ** 2
            else:
                pow[1] += bfs(i, j, 'B') ** 2

print(" ".join(map(str, pow)))