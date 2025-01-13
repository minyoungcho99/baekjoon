# 다리 만들기
import sys
from collections import deque

N = int(sys.stdin.readline())
board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

num = 1
visited = [[False] * N for _ in range(N)]
new_board = [[0] * N for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

info = [[], []]


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def bfs(sx, sy):
    visited[sx][sy] = True
    q = deque([(sx, sy)])
    new_board[sx][sy] = num
    info[num].append((sx, sy))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                new_board[nx][ny] = num
                info[num].append((nx,ny))
                q.append((nx, ny))


def find_min(n):
    q = deque([])
    for x, y in info[n]:
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and new_board[nx][ny] != n:
                visited[x][y] = True
                q.append((x, y, 1))
                break

    while q:
        x, y, dist = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and new_board[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny, dist+1))

            if in_range(nx, ny) and not visited[nx][ny] and (new_board[nx][ny] != 0 and new_board[nx][ny] != n):
                return dist - 1


for i in range(N):
    for j in range(N):
        if not visited[i][j] and board[i][j] == 1:
            bfs(i, j)
            num += 1
            info.append([])

min_dist = float('inf')

for i in range(1, num):
    visited = [[False] * N for _ in range(N)]
    min_dist = min(min_dist, find_min(i))

print(min_dist)