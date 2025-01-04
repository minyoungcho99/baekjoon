# 미세먼지 안녕!
import sys

R, C, T = map(int, sys.stdin.readline().split())
house = []
cleaner = []
time = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(R):
    house.append(list(map(int, sys.stdin.readline().split())))


def in_range(x, y):
    return 0 <= x < R and 0 <= y < C


def find():
    for i in range(R):
        if house[i][0] == -1:
            cleaner.append(i)


def spread():
    spread = [[0] * C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if house[x][y] > 0:
                cnt = 0
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if in_range(nx, ny) and house[nx][ny] != -1:
                        cnt += 1
                        spread[nx][ny] += house[x][y] // 5

                spread[x][y] += house[x][y] - (house[x][y] // 5) * cnt

    for x in range(R):
        for y in range(C):
            if spread[x][y] > 0:
                house[x][y] = spread[x][y]  # 동시 확산


def purify():
    upper, lower = cleaner[0], cleaner[1]
    purify = [[0] * C for _ in range(R)]

    # 위쪽 공기청정기 좌/우측
    for i in range(upper+1):
        if house[i][0] > 0:
            if house[i+1][0] != -1:
                purify[i+1][0] = house[i][0]

        if house[i][C-1] > 0:
            if in_range(i-1, C-1):
                purify[i-1][C-1] = house[i][C-1]

    # 위쪽 공기청정기 상/하단
    for j in range(C):
        if house[upper][j] > 0:
            if in_range(upper, j+1):
                purify[upper][j+1] = house[upper][j]

        if house[0][j] > 0:
            if in_range(0, j-1):
                purify[0][j-1] = house[0][j]

    # 아래쪽 공기청정기 좌/우측
    for i in range(lower, R):
        if house[i][0] > 0:
            if house[i-1][0] != -1:
                purify[i-1][0] = house[i][0]

        if house[i][C-1] > 0:
            if in_range(i+1, C-1):
                purify[i+1][C-1] = house[i][C-1]

    # 아래쪽 공기청정기 상/하단
    for j in range(C):
        if house[lower][j] > 0:
            if in_range(lower, j+1):
                purify[lower][j+1] = house[lower][j]

        if house[R-1][j] > 0:
            if in_range(R-1, j-1):
                purify[R-1][j-1] = house[R-1][j]

    # 붙이기 #

    # 위쪽 공기청정기 좌/우측
    for i in range(upper + 1):
        house[i][0] = purify[i][0]
        house[i][C-1] = purify[i][C-1]

    # 위쪽 공기청정기 상/하단
    for j in range(C):
        house[upper][j] = purify[upper][j]
        house[0][j] = purify[0][j]

    # 아래쪽 공기청정기 좌/우측
    for i in range(lower, R):
        house[i][0] = purify[i][0]
        house[i][C-1] = purify[i][C-1]

    # 아래쪽 공기청정기 상/하단
    for j in range(C):
        house[lower][j] = purify[lower][j]
        house[R-1][j] = purify[R-1][j]


def calculate():
    total = 0
    for i in range(R):
        for j in range(C):
            if house[i][j] > 0:
                total += house[i][j]

    return total


find()  # 공기청정기 위치

while time < T:
    spread()  # 미세먼지 확산
    purify()  # 공기청정기 작동

    for c in cleaner:
        house[c][0] = -1
        
    time += 1

print(calculate())