# 오목
import sys

board = []

for _ in range(19):
    board.append(list(map(int, sys.stdin.readline().split())))

visited = [[False] * 19 for _ in range(19)]

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

def bfs(sx, sy):
    dx = [0, 1, 1, -1]
    dy = [1, 0, 1, 1]
    cnt = 1

    for k in range(4):
        cnt = 1
        nx, ny = sx, sy

        if in_range(nx - dx[k], ny - dy[k]):
            if board[nx-dx[k]][ny-dy[k]] == board[nx][ny]:
                continue

        while True:
            nx, ny = nx+dx[k], ny+dy[k]
            if not in_range(nx, ny) or board[nx][ny] != board[sx][sy]:
                break
            cnt += 1

        if cnt == 5:
            return True

    return False


is_found = False
for i in range(19):
    for j in range(19):
        if board[i][j] > 0:
            if bfs(i, j):
                is_found = True
                print(board[i][j])
                print(" ".join(map(str, (i+1, j+1))))

if not is_found:
    print(0)