# 마법사 상어와 토네이도
import sys

N = int(sys.stdin.readline())
ans = 0
board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

percent = [[0, 0, 0.02, 0, 0],
           [0, 0.1, 0.07, 0.01, 0],
           [0.05, 0, 0, 0, 0],
           [0, 0.1, 0.07, 0.01, 0],
           [0, 0, 0.02, 0, 0]]

percents = [percent, [[0] * 5 for _ in range(5)], [[0] * 5 for _ in range(5)], [[0] * 5 for _ in range(5)]]

for i in range(5):
    for j in range(5):
        percents[3][j][4 - i] = percent[i][j]
        percents[2][4 - i][4 - j] = percent[i][j]
        percents[1][4 - j][i] = percent[i][j]


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def tornado():
    global ans
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    d = 0
    dist = 1
    move_cnt = 0

    x, y = N // 2, N // 2

    while True:
        for _ in range(dist):
            nx, ny = x + dx[d], y + dy[d]
            if (nx, ny) == (0, -1):
                print(ans)
                return

            alpha = board[nx][ny]
            if board[nx][ny] > 0:
                for i in range(5):
                    for j in range(5):
                        tx, ty = nx - 2 + i, ny - 2 + j
                        if percents[d][i][j] > 0:
                            if in_range(tx, ty):
                                board[tx][ty] += int(percents[d][i][j] * board[nx][ny])
                                alpha -= int(percents[d][i][j] * board[nx][ny])

                            else:
                                ans += int(percents[d][i][j] * board[nx][ny])
                                alpha -= int(percents[d][i][j] * board[nx][ny])

            ax, ay = nx + dx[d], ny + dy[d]
            if in_range(ax, ay):
                board[ax][ay] += alpha

            else:
                ans += alpha

            board[nx][ny] = 0
            x, y = nx, ny

        d = (d + 1) % 4
        move_cnt += 1

        if move_cnt == 2:
            dist += 1
            move_cnt = 0


tornado()