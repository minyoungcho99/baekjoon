# 알고스팟
import sys, heapq


def in_range(x, y):
    return 0 <= x < M and 0 <= y < N


def dijkstra(sx, sy):
    pq = []
    heapq.heappush(pq, (0, sx, sy))
    best[sx][sy] = 0

    while pq:
        dist, x, y = heapq.heappop(pq)

        if best[x][y] < dist:
            continue

        for nx, ny, ndist in adj_list[x][y]:
            if dist + ndist < best[nx][ny]:
                best[nx][ny] = dist + ndist
                heapq.heappush(pq, (dist+ndist, nx, ny))


N, M = map(int, sys.stdin.readline().split())
adj_list = [[[] for _ in range(N)] for _ in range(M)]
best = [[float('inf')] * N for _ in range(M)]

board = []
for _ in range(M):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for x in range(M):
    for y in range(N):
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny):
                adj_list[nx][ny].append((x, y, board[x][y]))

dijkstra(0, 0)
print(best[M-1][N-1])