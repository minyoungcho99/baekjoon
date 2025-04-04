import sys
from collections import deque

def in_range(mx, my):
    return 0 <= mx < R + 3 and 0 <= my < C

def is_out(mx):
    m = 0 <= mx < 3
    l = 0 <= mx + 1 < 3
    r = 0 <= mx - 1 < 3

    return m or l or r

def move(mx, my, dir):
    while True:
        can_move = False
        if mx + 1 == R + 2:
            break

        if in_range(mx+1, my-1) and in_range(mx+2, my) and in_range(mx+1, my+1) and \
                board[mx+1][my-1] == 0 and board[mx+2][my] == 0 and board[mx+1][my+1] == 0: # 남쪽 이동
            mx += 1
            can_move = True

        else:
            if in_range(mx-1, my-1) and in_range(mx+1, my-1) and in_range(mx+2, my-1) and \
                    in_range(mx, my-2) and in_range(mx + 1, my-2) and \
                board[mx - 1][my - 1] == 0 and board[mx + 1][my - 1] == 0 \
                    and board[mx + 2][my - 1] == 0 and board[mx][my - 2] == 0 and board[mx + 1][my - 2] == 0:
                mx += 1
                my -= 1
                dir = (dir - 1) % 4
                can_move = True

            else:
                if in_range(mx-1, my+1) and in_range(mx+1, my+1) and in_range(mx+2, my+1) and \
                    in_range(mx, my+2) and in_range(mx + 1, my+2) and \
                        board[mx - 1][my + 1] == 0 and board[mx + 1][my + 1] == 0 \
                        and board[mx + 2][my + 1] == 0 and board[mx][my + 2] == 0 and board[mx + 1][my + 2] == 0:
                    mx += 1
                    my += 1
                    dir = (dir + 1) % 4
                    can_move = True

        if not can_move:
            break

    return mx, my, dir

def mark_board(nx, ny, nd):
    board[nx][ny] = gidx
    for k in range(4):
        board[nx+dx[k]][ny+dy[k]] = gidx # 십자 모양 처리

    e_board[nx + dx[nd]][ny + dy[nd]] = gidx # 출구 처리

def escape(mx, my):
    max_r = 0
    visited = [[False] * C for _ in range(R + 3)]
    visited[mx][my] = True
    q = deque([(mx, my)])

    while q:
        # print(q)
        x, y = q.popleft()

        max_r = max(max_r, x-2)

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if not in_range(nx, ny) or visited[nx][ny]:
                continue
            if board[nx][ny] == board[x][y]:
                q.append((nx, ny))
                visited[nx][ny] = True
            else:
                if board[nx][ny] != 0:
                    if e_board[x][y] == board[x][y]:
                        q.append((nx, ny))
                        visited[nx][ny] = True


    return max_r

R, C, K = map(int, sys.stdin.readline().split())
board = [[0] * C for _ in range(R + 3)]
e_board = [[0] * C for _ in range(R + 3)]
g_list = [0] * (K + 1)
res = [0] * (K + 1)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, K + 1):
    c, d = map(int, sys.stdin.readline().split())
    g_list[i] =[1, c - 1, d]

for gidx in range(1, K + 1):
    # print(f"{gidx} started")
    mi, mj, d = g_list[gidx]
    # print(mi, mj)
    nmi, nmj, nd = move(mi, mj, d)
    # print("after")
    # print(nmi, nmj)

    if is_out(nmi):
        board = [[0] * C for _ in range(R + 3)]
        e_board = [[0] * C for _ in range(R + 3)]
        continue

    mark_board(nmi, nmj, nd)

    # for b in board:
    #     print(b)
    # print()
    # for e in e_board:
    #     print(e)

    g_list[gidx] = (nmi, nmj, nd)

    res[gidx] = escape(nmi, nmj)
    # print(res[gidx])

print(sum(res))
