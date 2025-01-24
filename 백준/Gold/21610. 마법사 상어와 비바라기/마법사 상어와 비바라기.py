# 마법사 상어와 비바라기
import sys

N, M = map(int, sys.stdin.readline().split())
A = []
moves = []
cloud = [[0] * N for _ in range(N)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]  # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

ddx = [-1, -1, 1, 1]  # ↖, ↗, ↘, ↙
ddy = [-1, 1, 1, -1]

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

for _ in range(M):
    d_i, s_i =  map(int, sys.stdin.readline().split())
    moves.append((d_i - 1, s_i))


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def move(d, s):
    new_cloud = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if cloud[i][j] > 0:
                new_cloud[(i + s * dx[d]) % N][(j + s * dy[d]) % N] = 1

    return new_cloud


def rain():
    for i in range(N):
        for j in range(N):
            if cloud[i][j] > 0:
                A[i][j] += 1


def copy():
    for i in range(N):
        for j in range(N):
            if cloud[i][j] > 0:

                temp = 0

                for k in range(4):
                    nx, ny = i + ddx[k], j + ddy[k]
                    if in_range(nx, ny) and A[nx][ny] > 0:
                        temp += 1

                A[i][j] += temp


for i, j in [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]:  # 비바라기 시전
    cloud[i][j] = 1


for d_i, s_i in moves:  # 이동
    cloud = move(d_i, s_i)  # 구름이 이동

    rain()
    copy()

    new_cloud = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and cloud[i][j] == 0:
                new_cloud[i][j] = 1
                A[i][j] -= 2

    cloud = new_cloud

ans = 0

for i in range(N):
    for j in range(N):
        ans += A[i][j]

print(ans)