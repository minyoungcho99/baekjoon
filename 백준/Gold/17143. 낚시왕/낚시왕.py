# 낚시왕
import sys


def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


def get():
    global ans
    for i in range(N):
        if len(board[i][king]) == 1:
            ans += board[i][king][0][2]  # 크기 추가
            board[i][king] = []  # 먹고 사라짐
            break

    return ans


def move_shark():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    result = [[[] for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if len(board[i][j]) == 1:
                s, d, z = board[i][j][0]
                board[i][j] = []

                nx, ny = i, j
                for _ in range(s):
                    nx += dx[d]
                    ny += dy[d]

                    if not in_range(nx, ny):
                        nx -= dx[d]
                        ny -= dy[d]

                        if d == 0 or d == 2:
                            d += 1
                        else:
                            d -= 1

                        nx += dx[d]
                        ny += dy[d]

                result[nx][ny].append([s, d, z])

    for i in range(N):
        for j in range(M):
            if len(result[i][j]) > 1:
                result[i][j].sort(key=lambda x: -x[2])
                result[i][j] = result[i][j][:1]

    return result


N, M, K = map(int, sys.stdin.readline().split())
board = [[[] for _ in range(M)] for _ in range(N)]

for _ in range(K):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    board[r-1][c-1].append([s, d-1, z])

king = 0
ans = 0
while True:
    if king == M:
        break

    get()
    board = move_shark()

    king += 1  # 낚시왕 이동

print(ans)