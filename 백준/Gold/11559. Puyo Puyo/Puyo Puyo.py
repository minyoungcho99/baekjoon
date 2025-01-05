# Puyo Puyo
import sys
from collections import deque
field = []

for _ in range(12):
    field.append(list(sys.stdin.readline().strip()))

# for f in field:
#     print(f)
#
# print()

combo = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def in_range(x, y):
    return 0 <= x < 12 and 0 <= y < 6


def bfs(sx, sy):
    visited[sx][sy] = True
    q = deque([(sx, sy)])
    locs = [(sx, sy)]

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and field[nx][ny] == field[x][y]:
                visited[nx][ny] = True
                locs.append((nx, ny))
                q.append((nx, ny))

    return locs if len(locs) >= 4 else []


def group(sx, sy):
    visited[sx][sy] = True
    q = deque([(sx, sy)])
    locs = [(sx, sy)]

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and field[nx][ny] == field[x][y]:
                visited[nx][ny] = True
                locs.append((nx, ny))
                q.append((nx, ny))

    for x, y in locs:
        if in_range(x+1, y):
            if field[x+1][y] == '.':
                return locs

    return []


def fall(locs):
    for x, y in locs:
        temp = field[x][y]
        field[x][y] = '.'

        while in_range(x+1, y) and field[x+1][y] == '.':
             x += 1

        field[x][y] = temp


while True:
    is_combo = False
    visited = [[0] * 6 for _ in range(12)]

    # 터지기
    for i in range(11, -1, -1):
        for j in range(6):
            if field[i][j] != '.':
                locs = bfs(i, j)

                if len(locs) != 0:
                    is_combo = True

                    for x, y in locs:
                        field[x][y] = '.'

    # for f in field:
    #     print(f)
    #
    # print()

    # 연쇄가 끊김
    if not is_combo:
        break

    combo += 1

    visited = [[0] * 6 for _ in range(12)]

    for i in range(11, -1, -1):
        for j in range(6):
            if field[i][j] != '.':
                locs = group(i, j)

                if len(locs) != 0:
                    fall(locs)

    # for f in field:
    #     print(f)
    #
    # print()

print(combo)