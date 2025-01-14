# 어른 상어
import sys
from collections import defaultdict

N, M, K = map(int, sys.stdin.readline().split())
board = []

shark = [0] * M
smell = [[0] * N for _ in range(N)]
priority = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

init_dir = list(map(int, sys.stdin.readline().split()))

for _ in range(M):
    sub_prior = []
    for _ in range(4):
        sub_prior.append(list(map(int, sys.stdin.readline().split())))

    priority.append(sub_prior)


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


class Shark:
    def __init__(self, num, x, y, dir):
        self.num = num
        self.x = x
        self.y = y
        self.dir = dir
        self.is_alive = True

    def pri(self):
        print(self.num, self.x, self.y, self.dir, self.is_alive)

    def next(self):
        num, x, y, dir = self.num, self.x, self.y, self.dir
        final_k = -1

        for k in priority[num][dir]:   # 인접한 방향에 냄새가 없는 칸이 있다면
            nx, ny = x + dx[k-1], y + dy[k-1]
            if in_range(nx, ny) and smell[nx][ny] == 0:
                final_k = k-1
                break

        if final_k == -1:   # 없다면
            for k in priority[num][dir]:
                nx, ny = x + dx[k-1], y + dy[k-1]
                if in_range(nx, ny) and smell[nx][ny] != 0:
                    if smell[nx][ny][0] == num:
                        final_k = k-1
                        break

        return final_k

    def set_info(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def set_alive(self):
        self.is_alive = False


for i in range(N):
    for j in range(N):
        num = board[i][j]
        if num != 0:
            shark[num-1] = Shark(num-1, i, j, init_dir[num-1] - 1)


def done():
    for s in shark:
        if s.num != 0 and s.is_alive:
            return False

    return True


time = 0

# 냄새 뿌리기
for s in shark:
    smell[s.x][s.y] = (s.num, K)

while True:
    if done():
        break

    if time == 1000:
        time = -1
        break

    # for s in shark:
    #     s.pri()

    checker = defaultdict(list)

    for s in shark:  # 이동 방향 결정
        if not s.is_alive:
            continue

        nd = s.next()
        nx, ny = s.x + dx[nd], s.y + dy[nd]
        s.set_info(nx, ny, nd)

    for s in shark:
        if not s.is_alive:
            continue

        num, sx, sy = s.num, s.x, s.y
        checker[(sx, sy)].append(num)

    for c in checker.values():  # 한 칸에 여러 마리 처리
        if len(c) > 1:
            for i in range(1, len(c)):
                num = c[i]
                shark[num].set_alive()

    for i in range(N):
        for j in range(N):
            if smell[i][j] != 0:
                num, l = smell[i][j]
                if l-1 != 0:
                    smell[i][j] = (num, l-1)
                else:
                    smell[i][j] = 0

    for s in shark:
        if not s.is_alive:
            continue

        num, sx, sy = s.num, s.x, s.y
        smell[sx][sy] = (num, K)

    # for s in smell:
    #     print(s)

    time += 1

print(time)