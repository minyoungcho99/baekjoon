import sys


def in_range(x, y):
    return 0 <= x < 8 and 0 <= y < 8


def check(x, y):
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    color = board[x][y]
    for k in range(8):
        is_ended = False
        opos = []
        nx, ny = x, y
        while True:
            nx, ny = nx+dx[k], ny+dy[k]
            if not in_range(nx, ny):
                break

            if board[nx][ny] == 0:
                break

            elif board[nx][ny] == color:
                is_ended = True
                break

            else:
                opos.append((nx, ny))

        if is_ended and len(opos) > 0:
            for ox, oy in opos:
                board[ox][oy] = color


def put(x, y, color):
    if color == 1: # 흑돌
        board[x][y] = 1
        check(x, y)

    else: # 백돌
        board[x][y] = 2
        check(x, y)


board = [[0] * 8 for _ in range(8)]
cmd = []

N = int(sys.stdin.readline())

for _ in range(N):
    cmd.append(tuple(map(int, sys.stdin.readline().split())))

for idx in range(N):
    if idx % 2 == 0: # 흑돌
        put(7-cmd[idx][1], cmd[idx][0], 1)

    else:
        put(7-cmd[idx][1], cmd[idx][0], 2)

for bor in board:
    for b in bor:
        if b == 0:
            print("_", end='')

        elif b == 1:
            print("@", end='')

        else:
            print("O", end='')
    print()
