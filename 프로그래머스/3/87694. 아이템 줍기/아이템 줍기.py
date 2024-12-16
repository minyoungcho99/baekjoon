# 아이템 줍기
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def in_range(x, y):
        return 0 <= x < 102 and 0 <= y < 102

    def bfs(cx, cy, ix, iy):
        cx *= 2
        cy *= 2

        ix *= 2
        iy *= 2
        visited[cy][cx] = 1
        q = deque([(cx, cy)])

        while q:
            x, y = q.popleft()

            if (x, y) == (ix, iy):
                return visited[y][x] // 2

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if in_range(nx, ny) and not visited[ny][nx] and map[ny][nx] == 1:

                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx, ny))

    map = [[0] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]

    for x1, y1, x2, y2 in rectangle: # 좌측하단 x1, y1, 우측상단 x2, y2
        x1 *= 2
        y1 *= 2

        x2 *= 2
        y2 *= 2
        # 테두리 처리
        for x in range(x1, x2+1): # 하단 가로, 상단 가로
            if map[y1][x] != 3: # 하단
                map[y1][x] = 1

            if map[y2][x] != 3: # 상단
                map[y2][x] = 1

        for y in range(y1, y2+1):
            if map[y][x1] != 3:  # 좌측
                map[y][x1] = 1

            if map[y][x2] != 3:  # 우측
                map[y][x2] = 1

        # 내부 처리
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                map[y][x] = 3

    # for m in map:
    #     print(m)

    # for v in visited:
    #     print(v)

    return bfs(characterX, characterY, itemX, itemY)