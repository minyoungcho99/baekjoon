# 코드트리 빵
import sys
from collections import deque

class Player:
    def __init__(self, pidx, x, y, fx, fy, is_reached):
        self.pidx = pidx
        self.x = x
        self.y = y
        self.fx = fx
        self.fy = fy
        self.is_reached = is_reached

    def move(self):
        global reached_list
        # visited = []
        # for k in range(4):
        #     nx, ny = self.x + dx[k], self.y + dy[k]
        #     if not in_range(nx, ny):
        #         continue
        #
        #     if abs(self.fx - nx) + abs(self.fy - ny) < abs(self.fx - self.x) + abs(self.fy - self.y) and not occupied[nx][ny]:
        #         self.x, self.y = nx, ny
        #         if (nx, ny) == (self.fx, self.fy):
        #             reached_list.append(self.pidx)
        #             self.is_reached = True
        #         break
        visited = [[False] * N for _ in range(N)]
        q = deque([(self.x, self.y, [])])
        visited[self.x][self.y] = True

        while q:
            x, y, trace = q.popleft()
            if (x, y) == (self.fx, self.fy):
                next_loc = trace[0]

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if in_range(nx, ny) and not visited[nx][ny] and not occupied[nx][ny]:
                    q.append((nx, ny, trace + [(nx, ny)]))
                    visited[nx][ny] = True

        self.x, self.y = next_loc[0], next_loc[1]
        if (self.x, self.y) == (self.fx, self.fy):
            self.is_reached = True
            reached_list.append(self.pidx)

    def find_base(self):
        visited = [[-1] * N for _ in range(N)]
        q = deque([(self.fx, self.fy)])
        visited[self.fx][self.fy] = 0
        min_route = 100
        base_locs = []
        while q:
            x, y = q.popleft()
            if board[x][y] == 1:
                if visited[x][y] > min_route:
                    break
    
                base_locs.append((x, y))
                min_route = visited[x][y]

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if in_range(nx, ny) and visited[nx][ny] == -1 and not occupied[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

        base_locs.sort(key=lambda x:(x[0], x[1]))
        rx, ry = base_locs[0][0], base_locs[0][1]
        self.x, self.y = rx, ry
        return rx, ry

    def print(self):
        print(f"player {self.pidx} at {self.x, self.y} is going to {self.fx, self.fy} convi")

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def all_reached():
    check = True
    for idx in range(1, M+1):
        if not players[idx].is_reached:
            check = False
            break

    return check

N, M = map(int, sys.stdin.readline().split())
board = []
occupied = [[False] * N for _ in range(N)] # 도착, 베이스캠프 점유 유무
players = [0]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, M+1):
    x, y = map(int, sys.stdin.readline().split())
    players.append(Player(i, None, None, x-1, y-1, False))

time = 1
while True:
    reached_list = []
    # print(f"{time} sec rn")
    # 1. 격자에 있는 사람들 모두 1칸 이동
    # for pidx in range(1, M+1):
    #     players[pidx].print()

    for pidx in range(1, M+1):
        if pidx < time and not players[pidx].is_reached:
            players[pidx].move()

    # 2. 도착한 사람 처리
    for ridx in reached_list:
        # occupied 처리
        occupied[players[ridx].x][players[ridx].y] = True

    # 3. 베이스캠프 처리
    if time <= M:
        bx, by = players[time].find_base()
        occupied[bx][by] = True

    if all_reached():
        break

    time += 1

print(time)
