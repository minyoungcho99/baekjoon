 # 연구소
import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, sys.stdin.readline().split())
board = []
max_cnt = float('-inf')

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))


def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


def count(temp):  # count the num of safety zones
    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                cnt += 1

    return cnt


def build():
    global max_cnt
    can_build = []

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                can_build.append((i, j))

    idx = [i for i in range(len(can_build))]

    for i in combinations(idx, 3):
        visited = [[False] * M for _ in range(N)]
        temp = deepcopy(board)

        temp[can_build[idx[i[0]]][0]][can_build[idx[i[0]]][1]] = 1
        temp[can_build[idx[i[1]]][0]][can_build[idx[i[1]]][1]] = 1
        temp[can_build[idx[i[2]]][0]][can_build[idx[i[2]]][1]] = 1

        for i in range(N):  # spreading out
            for j in range(M):
                if temp[i][j] == 2 and not visited[i][j]:
                    spread(i, j, temp)

        temp_cnt = count(temp)
        max_cnt = max(max_cnt, temp_cnt)


def spread(sx, sy, temp):
    visited = [[False] * M for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited[sx][sy] = True
    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and temp[nx][ny] == 0:
                q.append((nx, ny))
                temp[nx][ny] = 2
                visited[nx][ny] = True


build()
print(max_cnt)