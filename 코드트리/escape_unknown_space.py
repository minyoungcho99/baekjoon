# 미지의 공간 탈출
import sys
from collections import deque

def in_range_3d(x, y):
    return 0 <= x < M and 0 <= y < M

def in_range_2d(x, y):
    return 0 <= x < N and 0 <= y < N

def find_start_3d():
    for i in range(M):
        for j in range(M):
            if board3[4][i][j] == 2:
                return 4, i, j

def find_end_3d(ex2, ey2):
    sx2, sy2 = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 3:
                sx2, sy2 = i, j
                break

        if (sx2, sy2) != (0, 0):
            break

    if ey2 == sy2 - 1: # 서1
        return 1, M - 1, ex2 - sx2

    elif ey2 == sy2 + M: # 동0
        return 0, M - 1, M - 1 - (ex2 - sx2)

    elif ex2 == sx2 - 1: # 북3
        return 3, M - 1, M - 1 - (ey2 - sy2)

    else: # 남2
        return 2, M - 1, ey2 - sy2

def find_start_2d():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 3:
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if in_range_2d(ni, nj) and board[ni][nj] == 0:
                        return ni, nj

def find_end_2d():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 4:
                board[i][j] = 0
                return i, j

def bfs_3d():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[[-1] * M for _ in range(M)] for _ in range(5)]
    q = deque([(sz_3d, sx_3d, sy_3d)])
    visited[sz_3d][sx_3d][sy_3d] += 1

    while q:
        # print(q)
        # print()
        #
        # for v in visited:
        #     print(v)
        z, x, y = q.popleft()
        if (z, x, y) == (ez_3d, ex_3d, ey_3d):
            return visited[z][x][y]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range_3d(nx, ny):
                if visited[z][nx][ny] < 0 and board3[z][nx][ny] == 0:
                    q.append((z, nx, ny))
                    visited[z][nx][ny] = visited[z][x][y] + 1
            else:
                if nx < 0:
                    if z == 0:
                        nz, nx, ny = 4, M - 1 - ny, M - 1
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                    elif z == 1:
                        nz, nx, ny = 4, ny, 0
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                    elif z == 2:
                        nz, nx, ny = 4, M - 1, ny
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                    elif z == 3:
                        nz, nx, ny = 4, 0, M - 1 - ny
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                    else:
                        nz, nx, ny = 3, 0, M - 1 - ny
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                elif nx >= M:
                    if z == 4:
                        nz, nx, ny = 2, 0, ny
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                elif ny < 0:
                    if z == 0:
                        nz, nx, ny = 2, nx, M - 1
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                    elif z == 1:
                        nz, nx, ny = 3, nx, M - 1
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                    elif z == 2:
                        nz, nx, ny = 1, nx, M - 1
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((z, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                    elif z == 3:
                        nz, nx, ny = 0, nx, M - 1
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                    else:
                        nz, nx, ny = 1, 0, nx
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                else: # ny >= M
                    if z == 0:
                        nz, nx, ny = 3, nx, 0
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                    elif z == 1:
                        nz, nx, ny = 2, nx, 0
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                    elif z == 2:
                        nz, nx, ny = 0, nx, 0
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                    elif z == 3:
                        nz, nx, ny = 1, nx, 0
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

                    else:
                        nz, nx, ny = 0, 0, M - 1 - nx
                        if visited[nz][nx][ny] < 0 and board3[nz][nx][ny] == 0:
                            q.append((nz, nx, ny))
                            visited[nz][nx][ny] = visited[z][x][y] + 1

    return -1

def time_error():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    res = [[0] * N for _ in range(N)]

    for tx, ty, td, tv in times:
        res[tx][ty] = tv
        tx, ty = tx + dx[td], ty + dy[td]

        while in_range_2d(tx, ty) and board[tx][ty] == 0 and (tx, ty) != (ex_2d, ey_2d):
            res[tx][ty] = tv
            tv *= 2

            tx, ty = tx + dx[td], ty + dy[td]

    return res

def bfs_2d(d):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[0] * N for _ in range(N)]
    q = deque([(sx_2d, sy_2d)])
    visited[sx_2d][sy_2d] = d + 1

    while q:
        x, y = q.popleft()
        if (x, y) == (ex_2d, ey_2d):
            return visited[ex_2d][ey_2d]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range_2d(nx, ny) and not visited[nx][ny] and board[nx][ny] == 0:
                if error[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

                else:
                    if error[nx][ny] > visited[x][y] + 1:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1

    return -1

N, M, F = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
board3 = [[list(map(int, sys.stdin.readline().split())) for _ in range(M)] for _ in range(5)]
times = [list(map(int, sys.stdin.readline().split())) for _ in range(F)]

# 1. 주요 좌표 탐색 (3차원 시작, 3차원 도착, 2차원 시작, 2차원 도착)
sz_3d, sx_3d, sy_3d = find_start_3d()
sx_2d, sy_2d = find_start_2d()
ex_2d, ey_2d = find_end_2d()
ez_3d, ex_3d, ey_3d = find_end_3d(sx_2d, sy_2d)

# print(sx_2d, sy_2d)
# print(ex_2d, ey_2d)
# print(sz_3d, sx_3d, sy_3d)
# print(ez_3d, ex_3d, ey_3d)

# 2. 3차원(시간의 벽) 내 bfs (시작 위치 ~ 도착 위치)
dist = bfs_3d()

if dist != -1:
    # 3. 2차원(평면도) 내 bfs (시간 이상 현상 처리해서 시간 표시)
    error = time_error()

    # for e in error:
    #     print(e)

    dist = bfs_2d(dist)

print(dist)
