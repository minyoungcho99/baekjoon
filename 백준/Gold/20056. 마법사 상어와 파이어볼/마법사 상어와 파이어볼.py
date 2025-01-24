# 마법사 상어와 파이어볼
import sys

N, M, K = map(int, sys.stdin.readline().split())
board = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):
    r_i, c_i, m_i, s_i, d_i = map(int, sys.stdin.readline().split())
    board[r_i-1][c_i-1].append((m_i, s_i, d_i))

times = 0


def is_all(dl):
    for i in range(len(dl)):
        dl[i] %= 2

    if len(set(dl)) != 1:
        return False
    else:
        return True


while True:
    if times == K:
        break
    new_board = [[[] for _ in range(N)] for _ in range(N)]


    # 1. 이동
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 0:
                for m_i, s_i, d_i in board[i][j]:
                    new_board[(i + s_i * dx[d_i]) % N][(j + s_i * dy[d_i]) % N].append((m_i, s_i, d_i))

    board = new_board

    # 2. 같은 칸에 2개 이상 파이어볼일 시
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                weight = 0
                speed = 0
                ds = []

                for m_i, s_i, d_i in board[i][j]:
                    weight += m_i
                    speed += s_i
                    ds.append(d_i)

                weight //= 5
                speed //= len(board[i][j])

                board[i][j] = []

                if weight > 0: # 질량이 0보다 크다면
                    if is_all(ds):
                        for k in (0, 2, 4, 6):
                            board[i][j].append((weight, speed, k))

                    else:
                        for k in (1, 3, 5, 7):
                            board[i][j].append((weight, speed, k))

    times += 1

ans = 0
for i in range(N):
    for j in range(N):
        if len(board[i][j]) > 0:
            for m_i, _, _ in board[i][j]:
                ans += m_i

print(ans)