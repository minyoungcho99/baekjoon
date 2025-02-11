# 메이즈 러너
import sys
from copy import deepcopy

N, M, K = map(int, sys.stdin.readline().split())

board = []
player = []
dist = [0] * M
player_board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(M):
    px, py = map(int, sys.stdin.readline().split())
    player_board[px-1][py-1].append(i)
    player.append((px-1, py-1, False))

ex, ey = map(int, sys.stdin.readline().split())
ex -= 1
ey -= 1

board[ex][ey] = 10


def all_escaped():
    for i in range(M):
        if not player[i][2]:
            return False

    return True


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def move(pidx):
    # print(f"player {pidx}")
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    ox, oy = player[pidx][0], player[pidx][1]
    nx, ny = N+1, N+1

    for k in range(4):
        tx, ty = ox + dx[k], oy + dy[k]

        if in_range(tx, ty) and (not (1 <= board[tx][ty] <= 9)) and abs(ex-tx) + abs(ey-ty) < abs(ex-ox) + abs(ey-oy):
            nx, ny = tx, ty
            break

    if (nx, ny) != (N+1,N+1):  # 움직일 수 있으면
        if (nx, ny) == (ex, ey):  # 출구인 경우
            dist[pidx] += 1
            player[pidx] = (N+1, N+1, True)

        else:
            dist[pidx] += 1
            player[pidx] = (nx, ny, False)
            temp[nx][ny].append(pidx)

    else:
        temp[ox][oy].append(pidx)


def rotate(sx, sy, size):
    global ex, ey
    global board
    global player_board
    sub = [[0] * size for _ in range(size)]
    sub_p = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            sub[i][j] = board[sx+i][sy+j]
            sub_p[i][j] = player_board[sx+i][sy+j]

    temp = [[0] * size for _ in range(size)]
    temp_p = [[[] for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            temp[j][size-i-1] = sub[i][j]
            temp_p[j][size - i -1] = sub_p[i][j]

    for i in range(size):
        for j in range(size):
            if 1 <= temp[i][j] <= 9:
                temp[i][j] -= 1  # 내구도 감소

            if len(temp_p[i][j]) > 0:
                for p in temp_p[i][j]:
                    player[p] = (sx+i, sy+j, False)

    for i in range(size):
        for j in range(size):
            board[sx+i][sy+j] = temp[i][j]
            player_board[sx+i][sy+j] = temp_p[i][j]

    for i in range(sx, sx+size):
        for j in range(sy, sy+size):
            if board[i][j] == 10:
                ex, ey = i, j


for _ in range(K):
    # print(f"{_+1} round starts")
    if all_escaped():  # 모두 탈출했다면 게임 종료
        break

    # 플레이어 이동
    temp = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(M):
        if not player[i][2]:
            move(i)

    player_board = temp

    # print("***************")
    # for p in player_board:
    #     print(p)
    # print("**************")
    # for p in board:
    #     print(p)
    # print("****** rotation ******")
    # for p in player_board:
    #     print(p)

    rx, ry, rsize = 0, 0, 0
    # 미로 회전
    for size in range(2, N):
        for sx in range(N - size + 1):
            for sy in range(N - size + 1):
                p_exist = False
                e_exist = False

                for i in range(sx, sx+size):
                    for j in range(sy, sy+size):
                        if len(player_board[i][j]) > 0:
                            p_exist = True

                        if board[i][j] == 10:
                            e_exist = True

                if p_exist and e_exist:
                    rx, ry, rsize = sx, sy, size
                    break

            if (rx, ry, rsize) != (0, 0, 0):
                break

        if (rx, ry, rsize) != (0, 0, 0):
            break

    # print(rx, ry, rsize)
    rotate(rx, ry, rsize)

    # for p in player_board:
    #     print(p)
    #
    # for b in board:
    #     print(b)

    # print(player)
    # print(sum(dist))
print(sum(dist))
print(str(ex+1) + " " + str(ey+1))
