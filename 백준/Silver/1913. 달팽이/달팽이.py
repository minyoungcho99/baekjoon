# 달팽이
import sys

N = int(sys.stdin.readline())
target = int(sys.stdin.readline())


def tornado(n, t):
    board = [[0] * n for _ in range(n)]

    x, y, d = 0, 0, 0
    ax, ay = 0, 0
    for i in range(n*n, 0, -1):
        board[x][y] = i

        if i == target:
            ax, ay = x+1, y+1

        if d == 0:
            x += 1
            if x == n - 1 or board[x + 1][y] != 0:
                d = (d + 1) % 4

        elif d == 1:
            y += 1
            if y == n - 1 or board[x][y + 1] != 0:
                d = (d + 1) % 4

        elif d == 2:
            x -= 1
            if x == 0 or board[x - 1][y] != 0:
                d = (d + 1) % 4

        else:
            y -= 1
            if y == 0 or board[x][y - 1] != 0:
                d = (d + 1) % 4

    return board, (ax, ay)


board, ans= tornado(N, target)
for b in board:
    print(" ".join(map(str, b)))
print(" ".join(map(str, ans)))