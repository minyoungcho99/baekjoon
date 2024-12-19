# 아기 상어
import sys
from collections import deque

N = int(sys.stdin.readline())
board = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark = (i, j)
            board[i][j] = 0


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def find_next():
    q = deque([(shark[0], shark[1], 0)]) 
    visited = [[False] * N for _ in range(N)]
    visited[shark[0]][shark[1]] = True

    possible_fish = []
    while q:
        x, y, dist = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] <= weight:
                visited[nx][ny] = True
                if 0 < board[nx][ny] < weight:
                    possible_fish.append((dist + 1, nx, ny))
                q.append((nx, ny, dist + 1))

    if possible_fish:
        possible_fish.sort()
        return possible_fish[0] 
    
    else:
        return None  

time = 0
weight = 2
eaten_num = 0


while True:
    result = find_next()
    
    if not result:  # 먹을 물고기가 없으면 종료
        break

    dist, fx, fy = result

    # 상어 이동
    shark = (fx, fy)
    board[fx][fy] = 0
    eaten_num += 1

    # 크기 증가
    if eaten_num == weight:
        weight += 1
        eaten_num = 0

    # 시간 증가
    time += dist

print(time)