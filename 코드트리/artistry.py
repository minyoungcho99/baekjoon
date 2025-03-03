# 예술성
import sys
from collections import deque


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def adj(a, b):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    adj_q = deque()
    cnt = 0

    for i in range(N):
        for j in range(N):
            if grp_board[i][j] == a:
                adj_q.append((i, j))

    while adj_q:
        x, y = adj_q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and grp_board[nx][ny] == b:
                cnt += 1

    return cnt


def calculate(combi, tmp, idx):
    global point
    if len(tmp) == 2:
        a, b = grp[tmp[0]]
        c, d = grp[tmp[1]]
        point += (b+d) * a * c * adj(tmp[0], tmp[1])
        return

    for i in range(idx, len(combi)):
        calculate(combi, tmp + [combi[i]], i+1)

    return point


def sqr_rotate(sx, sy):
    temp = [[0] * (N//2) for _ in range(N//2)]
    for i in range(N//2):
        for j in range(N//2):
            temp[j][N // 2 - i - 1] = board[sx+i][sy+j]

    for i in range(N // 2):
        for j in range(N // 2):
            board[sx+i][sy+j] = temp[i][j]


def cross_rotate():
    temp = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            temp[N - 1 - j][i] = board[i][j]

    for i in range(N):
        board[N//2][i] = temp[N//2][i]
        board[i][N//2] = temp[i][N//2]


def bfs(sx, sy, i):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    visited[sx][sy] = True
    q = deque([(sx, sy)])
    grp_board[sx][sy] = i
    cnt = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
                grp_board[nx][ny] = i

    return cnt


N = int(sys.stdin.readline())
board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

ans = 0
for _ in range(4):
    grp = dict()
    visited = [[False] * N for _ in range(N)]
    grp_board = [[0] * N for _ in range(N)]

    grp_idx = 1
    grp_n = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                num = bfs(i, j, grp_idx)
                grp[grp_idx] = (board[i][j], num)
                grp_n += 1
                grp_idx += 1

    point = 0
    combi = [i for i in range(1, grp_n+1)]
    calculate(combi, [], 0)
    ans += point

    sqr_rotate(0,0)
    sqr_rotate(N//2+1, 0)
    sqr_rotate(0, N//2+1)
    sqr_rotate(N//2+1, N//2+1)

    cross_rotate()

print(ans)
