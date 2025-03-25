# 구슬 탈출 2
import sys
from collections import deque

def get_pos():
    global rx, ry, bx, by
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j

def move(x, y, d):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 0
    while board[x+dx[d]][y+dy[d]] != '#' and board[x][y] != 'O':
        x += dx[d]
        y += dy[d]
        cnt += 1

    return x, y, cnt

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if cnt > 10:
            break

        for k in range(4):
            nrx, nry, r_cnt = move(rx, ry, k)
            nbx, nby, b_cnt = move(bx, by, k)

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                return cnt

            if nbx == nrx and nby == nry:
                if r_cnt > b_cnt:
                    nrx -= dx[k]
                    nry -= dy[k]

                else:
                    nbx -= dx[k]
                    nby -= dy[k]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, cnt+1))

    return -1


N, M = map(int, sys.stdin.readline().split())
board = []
visited = set()
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

rx, ry, bx, by = 0, 0, 0, 0
get_pos()

q = deque([(rx, ry, bx, by, 1)])
visited.add((rx, ry, bx, by))
print(bfs())