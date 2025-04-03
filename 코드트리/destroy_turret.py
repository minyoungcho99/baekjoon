# 포탑 부수기
import sys
from collections import deque

def count():
    cnt = 0
    res = []

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                cnt += 1
                res.append((i, j))

    return res, cnt

def find_attacker(ulist):
    # 1. 공격력이 가장 낮은 포탑
    # 2. 가장 최근에 공격한 포탑
    # 3. 행과 열의 합이 가장 큰 포탑
    # 4. 열값이 가장 큰 포탑
    ulist.sort(key=lambda x: (board[x[0]][x[1]], time - attack_time[x[0]][x[1]], -(x[0] + x[1]), -x[1]))

    return ulist[0]

def find_receiver(ulist):
    # 1. 공격력이 가장 높은 포탑
    # 2. 가장 공격한 지 오래된 포탑
    # 3. 행과 열의 합이 가장 작은 포탑
    # 4. 열값이 가장 작은 포탑
    ulist.sort(key=lambda x: (-board[x[0]][x[1]], -(time - attack_time[x[0]][x[1]]), x[0] + x[1], x[1]))

    return ulist[0]

def get_route():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    visited = [[0] * M for _ in range(N)]

    q = deque([((ai, aj), [])])
    visited[ai][aj] = True

    while q:
        (i, j), route = q.popleft()

        for k in range(4):
            ni, nj = (i + dx[k]) % N, (j + dy[k]) % M
            if board[ni][nj] != 0 and not visited[ni][nj]:
                if (ni, nj) == (ri, rj):
                    return True, route

                else:
                    visited[ni][nj] = True
                    q.append(((ni, nj), route + [(ni, nj)]))

    return False, []

def laser(alist):
    global associated
    board[ri][rj] -= board[ai][aj]  # 공격 대상

    for i, j in alist: # 경로 내
        board[i][j] -= board[ai][aj] // 2

    for a in alist:
        associated.add(a)

def cannon():
    global associated
    dx = [-1, -1, -1, 1, 1, 1, 0, 0]
    dy = [-1, 0, 1, -1, 0, 1, -1, 1]

    board[ri][rj] -= board[ai][aj]  # 공격 대상
    for k in range(8):
        ni, nj = (ri + dx[k]) % N, (rj + dy[k]) % M
        if (ni, nj) != (ai, aj):
            board[ni][nj] -= board[ai][aj] // 2 # 주위 8방향
            associated.add((ni, nj))

def destroy():
    for i in range(N):
        for j in range(M):
            if board[i][j] < 0:
                board[i][j] = 0

def rebuild(alist):
    for i in range(N):
        for j in range(M):
            if (i, j) not in alist and board[i][j] != 0:
                board[i][j] += 1

N, M, K = map(int, sys.stdin.readline().split())
board = []
attack_time = [[0] * M for _ in range(N)]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for time in range(1, K+1):
    undestroyed, cnt = count()
    associated = set()

    if cnt == 1: # 부서지지 않은 포탑이 1개일 시 즉시 종료
        break

    # 1. 공격자 선정
    ai, aj = find_attacker(undestroyed)
    board[ai][aj] += N + M # 공격자 핸디캡
    attack_time[ai][aj] = time # 공격 시간 track
    associated.add((ai, aj)) # 공격에 관련된 포탑 track

    # 2. 공격 대상 선정
    undestroyed.remove((ai, aj)) # 공격자 제외
    ri, rj = find_receiver(undestroyed)
    associated.add((ri, rj))

    # 3. 공격 (레이저/포탑)
    can_attack, attack_list = get_route()
  
    if can_attack:
        laser(attack_list)

    else:
        cannon()

    # 4. 포탑 부서짐
    destroy()

    # 5. 포탑 정비
    rebuild(associated)

print(max(map(max, board)))
