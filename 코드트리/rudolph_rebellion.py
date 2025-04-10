# 루돌프의 반란
"""
디버깅한 부분

1. rudolph_move()
if board[rx][ry] > 0: # 루돌프가 도착한 곳에 산타가 존재
    idx = board[rx][ry]
    santa_list[idx].collide(True)

-> sx, sy에서 rx, ry 오타 고침

2. santa_list
for _ in range(P):
    sidx, sx, sy = map(int, sys.stdin.readline().split())
    santa_list[sidx] = Santa(sidx, sx-1, sy-1)
    board[sx-1][sy-1] = sidx
-> 입력이 santa 번호 오름차순으로 주어지는 줄 알았으나 번호는 무작위라서 그냥 append하지 않고 santa_list[i] = 으로 넣어줌

3. min_k = N 
 # 가장 가까워지는 방향으로 돌진
    dist = float('inf')
    min_k = N
    for k in range(8):
        nrx, nry = rx + dx[k], ry + dy[k]

        if (nrx-tx)**2 + (nry-ty)**2 < dist:
            dist = (nrx-tx)**2 + (nry-ty)**2
            min_k = k

    rx, ry = rx + dx[min_k], ry + dy[min_k]
    rd = min_k
-> dist = N가 보드 내에 최대 거리일 거라고 생각했는데 N 이상인 경우가 있나보다..? 
거리 기준이 맨해튼 거리(abs(x2-x1) + abs(y2-y1))가 아니기 때문에 N 이상이 될 수 있다! 따라서 float('inf')로 바꿔줌으로 해결함!
"""
import sys

class Santa:
    def __init__(self, sidx, sx, sy):
        self.sidx = sidx
        self.sx = sx
        self.sy = sy
        self.sd = 0
        self.is_fainted = False
        self.is_out = False

    def move(self):
        dist = (rx-self.sx)**2 + (ry-self.sy)**2
        min_k = -1

        for k in (0, 2, 4, 6): # 상 우 하 좌 우선순위
            nsx, nsy = self.sx + dx[k], self.sy + dy[k]
            # 범위 안이고, 다른 산타가 없고, 거리가 가까워지는 방향일 시
            if in_range(nsx, nsy) and not board[nsx][nsy] and (rx-nsx)**2 + (ry-nsy)**2 < dist:
                dist = (rx-nsx)**2 + (ry-nsy)**2
                min_k = k

        # 움직일 수 있다면 이동
        if min_k != -1:
            board[self.sx][self.sy] = 0
            self.sx, self.sy = self.sx + dx[min_k], self.sy + dy[min_k]
            board[self.sx][self.sy] = self.sidx
            self.sd = min_k

        if (rx, ry) == (self.sx, self.sy): # 충돌처리
            self.collide(False)

    def collide(self, is_rudolph):
        global score
        self.is_fainted = 2 # 기절 처리

        if is_rudolph: # 루돌프가 도착하여 충돌한 경우
            score[self.sidx] += C
            board[self.sx][self.sy] = 0
            self.sx, self.sy = self.sx + C * dx[rd], self.sy + C * dy[rd]

            if not in_range(self.sx, self.sy):
                self.is_out = True

            else:
                if board[self.sx][self.sy] > 0:  # 다른 산타가 있을 시
                    other = board[self.sx][self.sy]
                    board[self.sx][self.sy] = self.sidx
                    santa_list[other].interact(rd)

                else:
                    board[self.sx][self.sy] = self.sidx

        else: # 산타가 도착하여 충돌한 경우
            score[self.sidx] += D
            board[self.sx][self.sy] = 0
            self.sx, self.sy = self.sx + D * dx[(self.sd + 4) % 8], self.sy + D * dy[(self.sd + 4) % 8]

            if not in_range(self.sx, self.sy):
                self.is_out = True

            else:
                if board[self.sx][self.sy] > 0:  # 다른 산타가 있을 시
                    other = board[self.sx][self.sy]
                    board[self.sx][self.sy] = self.sidx
                    santa_list[other].interact((self.sd + 4) % 8)

                else:
                    board[self.sx][self.sy] = self.sidx

    def interact(self, dir):
        self.sx, self.sy = self.sx + dx[dir], self.sy + dy[dir]

        if not in_range(self.sx, self.sy):
            self.is_out = True

        else:
            if board[self.sx][self.sy] > 0:  # 다른 산타가 있을 시
                other = board[self.sx][self.sy]
                board[self.sx][self.sy] = self.sidx
                santa_list[other].interact(dir)

            else:
                board[self.sx][self.sy] = self.sidx

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def rudolph_move():
    global rx, ry, rd
    # 탈락하지 않은 산타 중 가장 가까운 산타 찾기
    temp = []
    for i in range(1, P+1):
        if not santa_list[i].is_out:
            temp.append(santa_list[i])

    temp.sort(key=lambda x: ((rx- x.sx)**2 + (ry-x.sy)**2, -x.sx, -x.sy))
    tx, ty = temp[0].sx, temp[0].sy

    # 가장 가까워지는 방향으로 돌진
    dist = float('inf')
    min_k = N
    for k in range(8):
        nrx, nry = rx + dx[k], ry + dy[k]

        if (nrx-tx)**2 + (nry-ty)**2 < dist:
            dist = (nrx-tx)**2 + (nry-ty)**2
            min_k = k

    rx, ry = rx + dx[min_k], ry + dy[min_k]
    rd = min_k

    if board[rx][ry] > 0: # 루돌프가 도착한 곳에 산타가 존재
        idx = board[rx][ry]
        santa_list[idx].collide(True)

def is_all_out():
    all_out = True
    for idx in range(1, P+1):
        if not santa_list[idx].is_out:
            all_out = False
            break

    return all_out

N, M, P, C, D = map(int, sys.stdin.readline().split())
rx, ry = map(int, sys.stdin.readline().split())

rx -= 1
ry -= 1
rd = 0

score = [0] * (P+1)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

board = [[0] * N for _ in range(N)]
santa_list = [0] * (P+1)
for _ in range(P):
    sidx, sx, sy = map(int, sys.stdin.readline().split())
    santa_list[sidx] = Santa(sidx, sx-1, sy-1)
    board[sx-1][sy-1] = sidx

for _ in range(M):
    # print(f"{_ + 1} turn started")
    if is_all_out():
        break

    rudolph_move()  # (1) 루돌프 움직임
    # print(rx, ry, rd)

    # (2) 산타 움직임
    for sidx in range(1, P + 1):
        if not santa_list[sidx].is_fainted and not santa_list[sidx].is_out:
            santa_list[sidx].move()
          
    # (3) 충돌 체크 및 기절/밀리기/상호작용

    # (4) 기절 카운트 줄이고 살아있는 산타에게 추가 점수 부여
    for sidx in range(1, P + 1):
        if not santa_list[sidx].is_out:
            score[sidx] += 1

            if santa_list[sidx].is_fainted > 0:
                santa_list[sidx].is_fainted -= 1

print(" ".join(map(str, score[1:])))
