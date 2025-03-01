import sys, heapq


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def dijkstra(sx, sy):
    pq = []
    heapq.heappush(pq, (board[sx][sy], sx, sy))
    best[sx][sy] = board[sx][sy]

    while pq:
        dist, x, y = heapq.heappop(pq)

        if best[x][y] < dist:
            continue

        for nx, ny, nd in adj_list[x][y]:
            if dist + nd < best[nx][ny]:
                best[nx][ny] = dist + nd
                heapq.heappush(pq, (dist+nd, nx, ny))


X, Y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
board = []
best = [[float('inf')] * N for _ in range(N)]
adj_list = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dx =[-1,1,0,0]
dy =[0,0,-1,1]
for i in range(N):
    for j in range(N):
        if board[i][j] != -1:
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if in_range(nx, ny):
                    adj_list[nx][ny].append((i, j, board[i][j]))


dijkstra(X, Y)
max_exh = 0
for i in range(N):
    for j in range(N):
        if type(best[i][j]) != float:
            max_exh = max(max_exh, best[i][j])

print(max_exh)
