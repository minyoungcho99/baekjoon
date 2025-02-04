# 연구소 2
import sys
from copy import deepcopy
from collections import deque

N, M = map(int, sys.stdin.readline().split())

comb = []
board = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def find_possible():
    temp = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                temp.append((i, j))

    return temp


def combination(temp, idx):
    global comb
    if len(temp) == M:
        comb.append(temp)
        return

    for i in range(idx, len(locs)):
        combination(temp + [i], i+1)


def check():
    for i in range(N):
        for j in range(N):
            if temp_board[i][j] == 0 or temp_board[i][j] == 2:
                return False

    return True


locs = find_possible()  # 바이러스 뿌릴 위치
combination([], 0)

min_time = float('inf')

for ci in range(len(comb)):
    temp_board = deepcopy(board)
    visited = [[False] * N for _ in range(N)]
    virus = [locs[i] for i in comb[ci]]

    t = 0
    q = deque([])
    for vx, vy in virus:
        q.append((vx, vy, t))
        visited[vx][vy] = True
        temp_board[vx][vy] = 3

    # print(q)

    while q:
        x, y, t = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and (temp_board[nx][ny] != 1):
                temp_board[nx][ny] = 3
                q.append((nx, ny, t+1))
                visited[nx][ny] = True

    # print("board after:")
    # for b in temp_board:
    #     print(b)

    if check():
        min_time = min(min_time, t)


if type(min_time) == float:
    print(-1)
else:
    print(min_time)
    