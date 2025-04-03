import sys
from collections import deque

def in_range(x, y):
    return 0 <= x < L and 0 <= y < L

def try_move(idx, d):
    q = deque()
    visited = [False] * (N + 1)

    temp_pos = knight[:]
    temp_damage = [0] * (N + 1)

    q.append(idx)
    visited[idx] = True

    while q:
        cur = q.popleft()
        r, c, h, w, k = temp_pos[cur]
        nr = r + dr[d]
        nc = c + dc[d]

        # 범위 체크
        if not in_range(nr, nc) or not in_range(nr + h - 1, nc + w - 1):
            return False

        # 벽 & 기사 충돌 체크
        for i in range(h):
            for j in range(w):
                x, y = nr + i, nc + j
                if board[x][y] == 2:
                    return False
                other = knight_board[x][y]
                if other != 0 and not visited[other] and other != cur:
                    q.append(other)
                    visited[other] = True

        temp_pos[cur] = [nr, nc, h, w, k]

    # 여기까지 오면 이동 가능
    for pid in range(1, N + 1):
        if not visited[pid] or not is_alive[pid]:
            continue

        r, c, h, w, _ = knight[pid]

        for i in range(h):
            for j in range(w):
                knight_board[r + i][c + j] = 0

    for pid in range(1, N + 1):
        if not visited[pid] or not is_alive[pid]:
            continue

        r, c, h, w, k = temp_pos[pid]
        knight[pid] = [r, c, h, w, k]

        for i in range(h):
            for j in range(w):
                x, y = r + i, c + j
                knight_board[x][y] = pid
                if board[x][y] == 1 and pid != idx:
                    temp_damage[pid] += 1

        damage[pid] += temp_damage[pid]

    return True

def move(idx, d):
    if is_alive[idx]:
        try_move(idx, d)


def alive_check():
    for i in range(1, N+1):
        if damage[i] >= knight[i][4]:
            is_alive[i] = False

            r, c, h, w, k = knight[i]

            for i in range(h):
                for j in range(w):
                    knight_board[r+i][c+j] = 0

# 입력
L, N, Q = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(L)]

knight = [0] * (N + 1)
damage = [0] * (N + 1)
is_alive = [True] * (N + 1)
knight_board = [[0] * L for _ in range(L)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    knight[i] = [r-1, c-1, h, w, k]
    for x in range(h):
        for y in range(w):
            knight_board[r-1 + x][c-1 + y] = i

for _ in range(Q):
    i, d = map(int, input().split())
    move(i, d)
    alive_check()

ans = 0
for i in range(1, N + 1):
    if is_alive[i]:
        ans += damage[i]

print(ans)
