"""
** 디버깅한 부분 **
(1) 탐사 진행 시 열 작은 거 -> 행 작은 거 해야되는데 반대로 함
(2) 1턴에서 획득한 개수가 0일 때 아예 탐사 종료 해줘야 하는데 안함
문제를 제발읽자~~
"""
# 고대 문명 유적 탐사
import sys
from collections import deque
from copy import deepcopy

K, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(5):
    board.append(list(map(int, sys.stdin.readline().split())))

piece = list(map(int, sys.stdin.readline().split()))


def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def bfs(sx, sy, b, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[sx][sy] = True
    q = deque([(sx, sy)])
    cnt = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and b[nx][ny] == b[x][y]:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt


def find_loc(sx, sy):
    temp = [(sx, sy)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[sx][sy] = True
    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                q.append((nx, ny))
                visited[nx][ny] = True
                temp.append((nx, ny))

    return temp


def rotate(mx, my, ang):
    sub_board = [[0] * 3 for _ in range(3)]
    for x in range(3):
        for y in range(3):
            sub_board[x][y] = board[mx-1+x][my-1+y]

    for _ in range(ang):
        new_board = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                new_board[j][2-i] = sub_board[i][j]

        for i in range(3):
            for j in range(3):
                sub_board[i][j] = new_board[i][j]

    rotated = deepcopy(board)
    for x in range(3):
        for y in range(3):
            rotated[mx-1+x][my-1+y] = sub_board[x][y]

    return rotated


def explore():
    lst = []
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                temp_val = 0
                temp_board = rotate(i, j, k)
                visited = [[0] * 5 for _ in range(5)]

                for r in range(5):
                    for c in range(5):
                        if not visited[r][c]:
                            tmp = bfs(r, c, temp_board, visited)

                            if tmp >= 3:
                                temp_val += tmp

                lst.append((temp_val, k, i, j))

    lst.sort(key=lambda x:(-x[0], x[1], x[3], x[2]))
    fk, fi, fj = lst[0][1], lst[0][2], lst[0][3]

    rotated = rotate(fi, fj, fk)
    for i in range(5):
        for j in range(5):
            board[i][j] = rotated[i][j]


def generate(l):
    global idx

    for lx, ly in l:
        idx += 1
        board[lx][ly] = piece[idx % M]


idx = -1

for _ in range(K):
    cnt = 0
    explore()  # 탐사 진행
    visited = [[0] * 5 for _ in range(5)]

    locs = []
    for j in range(5):
        for i in range(5):
            if not visited[i][j]:
                lst = find_loc(i, j)

                if len(lst) >= 3:
                    for l in lst:
                        locs.append(l)


    cnt += len(locs)
    locs.sort(key=lambda x: (x[1], -x[0]))
    generate(locs) # 유물 1차 획득

    while True:
        visited = [[0] * 5 for _ in range(5)]

        locs = []
        for i in range(5):
            for j in range(5):
                if not visited[i][j]:
                    lst = find_loc(i, j)

                    if len(lst) >= 3:
                        for l in lst:
                            locs.append(l)

        if len(locs) == 0:
            break

        cnt += len(locs)
        locs.sort(key=lambda x: (x[1], -x[0]))

        generate(locs)  # 유물 연쇄 획득

    if cnt != 0:
        print(cnt, end=' ')

    else:
        break
