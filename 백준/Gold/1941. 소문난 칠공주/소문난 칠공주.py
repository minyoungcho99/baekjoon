# 소문난 칠공주
import sys
from collections import deque

ans = 0
board = []
locs = [(i, j) for i in range(5) for j in range(5)]

for _ in range(5):
    board.append(list(sys.stdin.readline().rstrip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def combination(temp, i):
    global ans
    if len(temp) == 7:
        cnt = 0
        for t in temp:
            if board[t[0]][t[1]] == 'S':
                cnt += 1

        if cnt >= 4 and is_connected(temp):
            ans += 1
        return

    for idx in range(i, len(locs)):
        combination(temp + [locs[idx]], idx+1)


def is_connected(possible):
    q = deque([possible[0]])
    possible.remove(possible[0])

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and (nx, ny) in possible:
                q.append((nx, ny))
                possible.remove((nx, ny))

    if len(possible) == 0:
        return True
    else:
        return False

combination([], 0)
print(ans)