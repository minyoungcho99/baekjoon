import sys


def in_range(x, y):
    return 0 <= x < 6 and 0 <= y < 6


def shoot(c, d):
    dx = [-1,-1,1,1]
    dy = [-1,1,1,-1]
    visited = [[False] * 6 for _ in range(6)]

    x, y = 5, c
    strg = 1
    if d == 'L':
        k = 0
        if (canvas[x][y] == 0 or canvas[x][y]) >= strg and not visited[x][y]:
            canvas[x][y] = strg
            visited[x][y] = True
            strg += 1

        nx, ny = x, y
        while True:
            nx, ny = nx+dx[k], ny+dy[k]
            while not in_range(nx, ny):
                nx, ny = nx - dx[k], ny - dy[k]
                k = (k + 1) % 4
                nx, ny = nx + dx[k], ny + dy[k]

            if visited[nx][ny]:
                break

            else:
                if canvas[nx][ny] == 0 or canvas[nx][ny] >= strg:
                    canvas[nx][ny] = strg
                    visited[nx][ny] = True
                    strg += 1

                else:
                    visited[nx][ny] = True
                    strg += 1
    else:
        k = 1
        if (canvas[x][y] == 0 or canvas[x][y] >= strg) and not visited[x][y]:
            canvas[x][y] = strg
            visited[x][y] = True
            strg += 1

        nx, ny = x, y
        while True:
            nx, ny = nx + dx[k], ny + dy[k]
            while not in_range(nx, ny):
                nx, ny = nx - dx[k], ny - dy[k]
                k = (k - 1) % 4
                nx, ny = nx + dx[k], ny + dy[k]

            if visited[nx][ny]:
                break

            else:
                if canvas[nx][ny] == 0 or canvas[nx][ny] >= strg:
                    canvas[nx][ny] = strg
                    visited[nx][ny] = True
                    strg += 1

                else:
                    visited[nx][ny] = True
                    strg += 1


N = int(sys.stdin.readline())
canvas = [[0] * 6 for _ in range(6)]

for _ in range(N):
    col, dir = sys.stdin.readline().rstrip().split()
    shoot(int(col), dir)

for can in canvas:
    for c in can:
        if c == 0:
            print("_", end='')
        else:
            print(c, end='')
    print()
