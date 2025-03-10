"""
디버깅한 부분
1. 참가자는 주어진 판들을 시계 방향, 혹은 반시계 방향으로 자유롭게 회전할 수 있다. 
회전을 완료한 후 참가자는 판 5개를 쌓는다. 판을 쌓는 순서는 참가자가 자유롭게 정할 수 있다. 

-> 따라서 각각의 판은 0도, 90도, 180도, 270도 회전할 수 있고
각각의 판을 순서대로 쌓는 경우까지 해줘야 됨
문제를 안 읽어서 판의 순서 부분을 구현을 하지 않음


2. 
def permutation_layer(temp):
    if len(temp) == 5:
        permu_layer.append(temp)
        return

    for i in range(5):
        if not visited[i]:
            visited[i] = True
            permutation_layer(temp + [rr[i]])
            visited[i] = False

회전 순열을 구하는 경우에는 판끼리 돌리는 정도가 겹쳐도 괜찮지만 (중복순열)
쌓는 순열을 구할 때는 한 칸에 하나의 판씩 들어가야 해서 visited가 필요함 (permutation w/o repetition)
"""

# Maaaaaaaaaze
import sys
from collections import deque


def in_range(z, x, y):
    return 0 <= z < 5 and 0 <= x < 5 and 0 <= y < 5


def permutation(temp):
    if len(temp) == 5:
        permu.append(temp)
        return

    for i in range(4):
        permutation(temp + [r[i]])


def permutation_layer(temp):
    if len(temp) == 5:
        permu_layer.append(temp)
        return

    for i in range(5):
        if not visited[i]:
            visited[i] = True
            permutation_layer(temp + [rr[i]])
            visited[i] = False


def rotate(idx, dir):
    temp = [[0] * 5 for _ in range(5)]

    if dir == 0:
        for i in range(5):
            for j in range(5):
                temp[i][j] = cube[idx][i][j]

    elif dir == 1:
        for i in range(5):
            for j in range(5):
                temp[j][4-i] = cube[idx][i][j]

    elif dir == 2:
        for i in range(5):
            for j in range(5):
                temp[4-i][4-j] = cube[idx][i][j]

    else:
        for i in range(5):
            for j in range(5):
                temp[4-j][i] = cube[idx][i][j]

    return temp


def bfs(c):
    if c[sz][sx][sy] == 0 or c[fz][fx][fy] == 0:
        return -1

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visited[sz][sx][sy] += 1
    q = deque([(sz, sx, sy)])

    while q:
        z, x, y = q.popleft()
        if (z, x, y) == (fz, fx, fy):
            return visited[z][x][y]

        for k in range(6):
            nz, nx, ny = z + dz[k], x + dx[k], y + dy[k]
            if in_range(nz, nx, ny) and visited[nz][nx][ny] == 0 and c[nz][nx][ny] == 1:
                visited[nz][nx][ny] = visited[z][x][y] + 1
                q.append((nz, nx, ny))

    return -1


cube = []
for _ in range(5):
    sub_cube = []
    for _ in range(5):
        sub_cube.append(list(map(int, sys.stdin.readline().split())))

    cube.append(sub_cube)

r = [0, 1, 2, 3]
rr = [0, 1, 2, 3, 4]
visited = [0] * 5

permu = []
permu_layer = []
min_dist = float('inf')

permutation([])
permutation_layer([])

sz, sx, sy = 0, 0, 0
fz, fx, fy = 4, 4, 4

rotates = [[] for _ in range(5)]
for i in range(5):
    for j in range(4):
        rotates[i].append(rotate(i, j))

for p0, p1, p2, p3, p4 in permu:
    temp_cube = [0, 0, 0, 0, 0]
    for l0, l1, l2, l3, l4 in permu_layer:
        temp_cube[l0] = rotates[0][p0]
        temp_cube[l1] = rotates[1][p1]
        temp_cube[l2] = rotates[2][p2]
        temp_cube[l3] = rotates[3][p3]
        temp_cube[l4] = rotates[4][p4]

        temp_dist = bfs(temp_cube)
        if temp_dist != -1:
            min_dist = min(min_dist, temp_dist)

if type(min_dist) == float:
    print(-1)

else:
    print(min_dist-1)
