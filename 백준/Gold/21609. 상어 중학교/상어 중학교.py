# 상어 중학교
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

score = 0
grps = []
board = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))


class Group:
    def __init__(self, n, n_rainbow, main_block, crds):
        self.n = n
        self.n_rainbow = n_rainbow
        self.main_block = main_block
        self.crds = crds

    def remove(self):
        for i, j in self.crds:
            board[i][j] = -3

    def print(self):
        print(f"nums: {self.n}, rainbow_nums: {self.n_rainbow}, main_block: {self.main_block}, crds: {self.crds}")


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def find_grps(sx, sy):  # 크기가 가장 큰 블록 그룹을 찾음
    global grps
    crds = [(sx, sy)]
    colors = [(sx, sy)]
    color = board[sx][sy]

    visited = [[False] * N for _ in range(N)]

    visited[sx][sy] = True
    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == color:  # 일반 블럭일 때
                    crds.append((nx, ny))
                    colors.append((nx, ny))
                    visited[nx][ny] = True
                    q.append((nx, ny))

            elif in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == 0:  # 무지개 블럭일 때
                    crds.append((nx, ny))
                    visited[nx][ny] = True
                    q.append((nx, ny))

    if len(crds) >= 2:
        colors.sort() # 일반 블럭 중 행번호 가장 작고, 열번호가 가장 작은 블록
        grps.append(Group(n=len(crds), n_rainbow=len(crds) - len(colors), main_block=colors[0], crds=crds))


def gravity():  # 중력
    for i in range(N-1):
        for j in range(N):
            p = i
            while 0 <= p and (board[p][j] != -1 and board[p][j] != -3) and board[p+1][j] == -3: # -1 빼고 일
                board[p][j], board[p+1][j] = board[p+1][j], board[p][j]
                p -= 1


def rotate():  # 90도 반시계 회전
    new_board = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[j][N-1-i]

    return new_board


while True:
    grps = []
    for i in range(N):
        for j in range(N):
            if board[i][j] <= 0: continue  # 검은색 블럭, 무지개 블럭, 빈 칸일 때

            else: # 일반 블럭일 때
                find_grps(i, j)

    if len(grps) == 0:
        break

    grps.sort(key=lambda x: (x.n, x.n_rainbow, (x.main_block[0], x.main_block[1])))

    # for g in grps:
    #     g.print()
    #
    # print()

    grps[-1].remove()

    score += (grps[-1].n) ** 2

    gravity()

    rotated = rotate()
    board = rotated

    # for b in board:
    #     print(b)
    #
    # print()

    gravity()

    # for b in board:
    #     print(b)
    #
    # print()

print(score)