"""
# 디버깅한 부분
1. move_lose()
    if gun_map[nx][ny]: # 없을 때는 pop()하지 않도록 추가
        gun_map[nx][ny].sort()
        self.gun = gun_map[nx][ny].pop() 

2. move_lose()
    n, (x, y), d, g = self.num, self.loc, self.dir, self.gun

    nx, ny = x + dx[d], y + dy[d]
    while not in_range(nx, ny) or len(player_map[(nx, ny)]) > 0:  # 이동 방향으로 움직일 때 격자 범위 밖이거나 다른 플레이어가 있으면
        self.dir = (self.dir + 1) % 4
        d = self.dir
        nx, ny = x + dx[d], y + dy[d]

    # 이동 시 player_map[(x, y)].remove/append(i) 
    # move_lose()을 호출한 instance의 self.num(n)을 append/remove해야 하는데 i로 헷갈림
    # 이동해서 battle()을 trigger하는 i번째 instance가 무조건 져서 이동하도록 함
    player_map[(x, y)].remove(n)
    self.loc = (nx, ny)
    player_map[(nx, ny)].append(n)
"""
# 싸움땅
import sys
from collections import defaultdict

N, M, K = map(int, sys.stdin.readline().split())

pt = [0] * M

temp_map = []
for _ in range(N):
    temp_map.append(list(map(int, sys.stdin.readline().split())))

gun_map = [[[] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        gun_map[i][j].append(temp_map[i][j])


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


class Player:
    def __init__(self, num, loc, dir, power):
        self.num = num
        self.loc = loc
        self.dir = dir
        self.power = power
        self.gun = 0

    def print(self):
        print(f"Player {self.num} at {self.loc} has {self.dir} direction and {self.power} power with {self.gun} gun.")

    def move(self):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n, (x, y), d, g = self.num, self.loc, self.dir, self.gun

        nx, ny = x + dx[d], y + dy[d]
        if not in_range(nx, ny):  # 이동 방향으로 나갈 때 격자를 벗어나는 경우 방향 정반대
            self.dir = (self.dir + 2) % 4
            d = self.dir
            nx, ny = x + dx[d], y + dy[d]

        # 이동
        player_map[(x, y)].remove(i)
        self.loc = (nx, ny)
        player_map[(nx, ny)].append(i)

        if len(player_map[(nx, ny)]) == 1:  # 다른 플레이어가 없다면
            if g == 0 and gun_map[nx][ny]:  # 총을 들고 있지 않고 이동한 위치에 총이 있다면
                gun_map[nx][ny].sort()
                self.gun = gun_map[nx][ny].pop()  # 정렬 후 제일 큰 것 줍기

            elif g != 0 and gun_map[nx][ny]:  # 총을 들고 있고 이동한 위치에 총이 있다면
                gun_map[nx][ny].append(g)
                gun_map[nx][ny].sort()
                self.gun = gun_map[nx][ny].pop()  # 정렬 후 제일 큰 것 줍기

        else:  # 다른 플레이어가 있다면
            player_list[n].battle()

    def move_lose(self):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n, (x, y), d, g = self.num, self.loc, self.dir, self.gun

        nx, ny = x + dx[d], y + dy[d]
        while not in_range(nx, ny) or len(player_map[(nx, ny)]) > 0:  # 이동 방향으로 움직일 때 격자 범위 밖이거나 다른 플레이어가 있으면
            self.dir = (self.dir + 1) % 4
            d = self.dir
            nx, ny = x + dx[d], y + dy[d]

        # 이동
        player_map[(x, y)].remove(n)
        self.loc = (nx, ny)
        player_map[(nx, ny)].append(n)

        if gun_map[nx][ny]:
            gun_map[nx][ny].sort()
            self.gun = gun_map[nx][ny].pop()  # 정렬 후 제일 큰 것 줍기

    def battle(self):
        dx = [-1, 0, 0, 1]
        dy = [0, 1, -1, 0]

        opponent = None
        x, y = self.loc

        for i in player_map[(x, y)]:
            if i != self.num:
                opponent = player_list[i]

        if self.gun + self.power > opponent.gun + opponent.power:
            # self: 이긴 플레이어, opponent: 진 플레이어
            pt[self.num] += abs(self.gun + self.power - opponent.gun - opponent.power)

            # 진 플레이어 총 떨어트리고 이동
            if opponent.gun != 0:
                gun_map[x][y].append(opponent.gun)
                gun_map[x][y].sort()

                opponent.gun = 0

            opponent.move_lose()

            # 이긴 플레이어 총 줍기
            if self.gun == 0 and gun_map[x][y]:  # 총을 들고 있지 않고 이동한 위치에 총이 있다면
                gun_map[x][y].sort()
                self.gun = gun_map[x][y].pop()  # 정렬 후 제일 큰 것 줍기

            elif self.gun != 0 and gun_map[x][y]:  # 총을 들고 있고 이동한 위치에 총이 있다면
                gun_map[x][y].append(self.gun)
                gun_map[x][y].sort()
                self.gun = gun_map[x][y].pop()  # 정렬 후 제일 큰 것 줍기

        elif self.gun + self.power == opponent.gun + opponent.power:
            if self.power > opponent.power:
                # 진 플레이어 총 떨어트리고 이동
                if opponent.gun != 0:
                    gun_map[x][y].append(opponent.gun)
                    gun_map[x][y].sort()

                    opponent.gun = 0

                opponent.move_lose()

                # 이긴 플레이어 총 줍기
                if self.gun == 0 and gun_map[x][y]:  # 총을 들고 있지 않고 이동한 위치에 총이 있다면
                    gun_map[x][y].sort()
                    self.gun = gun_map[x][y].pop()  # 정렬 후 제일 큰 것 줍기

                elif self.gun != 0 and gun_map[x][y]:  # 총을 들고 있고 이동한 위치에 총이 있다면
                    gun_map[x][y].append(self.gun)
                    gun_map[x][y].sort()
                    self.gun = gun_map[x][y].pop()  # 정렬 후 제일 큰 것 줍기

            else:
                # 진 플레이어 총 떨어트리고 이동
                if self.gun != 0:
                    gun_map[x][y].append(self.gun)
                    gun_map[x][y].sort()

                    self.gun = 0

                self.move_lose()

                # 이긴 플레이어 총 줍기
                x, y = opponent.loc
                if opponent.gun == 0 and gun_map[x][y]:  # 총을 들고 있지 않고 이동한 위치에 총이 있다면
                    gun_map[x][y].sort()
                    opponent.gun = gun_map[x][y].pop()  # 정렬 후 제일 큰 것 줍기

                elif opponent.gun != 0 and gun_map[x][y]:  # 총을 들고 있고 이동한 위치에 총이 있다면
                    gun_map[x][y].append(opponent.gun)
                    gun_map[x][y].sort()
                    opponent.gun = gun_map[x][y].pop()  # 정렬 후 제일 큰 것 줍기

        else:
            # self: 진 플레이어, opponent: 이긴 플레이어
            pt[opponent.num] += abs(self.gun + self.power - opponent.gun - opponent.power)

            # 진 플레이어 총 떨어트리고 이동
            if self.gun != 0:
                gun_map[x][y].append(self.gun)
                gun_map[x][y].sort()

                self.gun = 0

            self.move_lose()

            # 이긴 플레이어 총 줍기
            x, y = opponent.loc
            if opponent.gun == 0 and gun_map[x][y]:  # 총을 들고 있지 않고 이동한 위치에 총이 있다면
                gun_map[x][y].sort()
                opponent.gun = gun_map[x][y].pop()  # 정렬 후 제일 큰 것 줍기

            elif opponent.gun != 0 and gun_map[x][y]:  # 총을 들고 있고 이동한 위치에 총이 있다면
                gun_map[x][y].append(opponent.gun)
                gun_map[x][y].sort()
                opponent.gun = gun_map[x][y].pop()  # 정렬 후 제일 큰 것 줍기


player_map = defaultdict(list)
player_list = []

for i in range(M):
    x, y, d, s = map(int, sys.stdin.readline().split())
    player_list.append(Player(i, (x-1, y-1), d, s))
    player_map[(x-1, y-1)].append(i)


for _ in range(K):  # K 라운드
    # print(f"{_+1} round")
    for i in range(M):
        player_list[i].move()
        # print(f"after player {i} turn")
        # print(player_map)

print(" ".join(map(str, pt)))
