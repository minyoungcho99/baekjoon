import sys, heapq


def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


def dijkstra(sx, sy):
    pq = []
    heapq.heappush(pq, (board[0][0], sx, sy))
    best[sx][sy] = board[0][0]

    while pq:
        dist, x, y = heapq.heappop(pq)

        if best[x][y] < dist:
            continue

        for nx, ny, nd in adj_list[x][y]:
            if dist + nd < best[nx][ny]:
                best[nx][ny] = dist + nd
                heapq.heappush(pq, (dist + nd, nx, ny))


N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

adj_list = [[[] for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(M):
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if in_range(nx, ny):
                adj_list[nx][ny].append((i, j, board[i][j]))

best = [[float('inf')] * M for _ in range(N)]

dijkstra(0, 0)
print(best[N-1][M-1])
