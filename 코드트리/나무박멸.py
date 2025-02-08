"""
# 틀린 부분
1. spread()
    if max_tree != -1:
        ans += max_tree

        tree[max_loc[0]][max_loc[1]] = 0
        treekiller[max_loc[0]][max_loc[1]] = C + 1

        for k in range(4):
            for time in range(1, K+1):
                nx, ny = max_loc[0] + ddx[k] * time, max_loc[1] + ddy[k] * time

                if not in_range(nx, ny) or tree[nx][ny] == -1:
                    break

                if tree[nx][ny] == 0:
                    treekiller[nx][ny] = C+1
                    break

                tree[nx][ny] = 0
                treekiller[nx][ny] = C+1
                
# tree[nx][ny] == 0(비어있는 칸)일 때는 treekiller[nx][ny]에 C+1 년만큼 뿌리고 움직임을 멈춰줘야 하는데
# if not in_range(nx, ny) or tree[nx][ny] < 0:
#    break
# 이렇게 해서 비어있는 칸일 때 안 뿌리고 움직임을 멈춤
"""
# 나무박멸
import sys

N, M, K, C = map(int, sys.stdin.readline().split())

ans = 0
tree = []
treekiller = [[0] * N for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ddx = [-1, -1, 1, 1]
ddy = [-1, 1, -1, 1]

for _ in range(N):
    tree.append(list(map(int, sys.stdin.readline().split())))


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def grow():
    temp = [[0] * N for _ in range(N)]
    for i in range(N):  # 인접 4칸 중 나무가 있는 칸 수만큼 나무 성장
        for j in range(N):
            if tree[i][j] > 0:
                num = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]

                    if in_range(nx, ny) and tree[nx][ny] > 0:
                        num += 1

                if num > 0:
                    temp[i][j] += num

    for i in range(N):  # 동시에 성장
        for j in range(N):
            if temp[i][j] > 0:
                tree[i][j] += temp[i][j]


def breed():
    temp = [[0] * N for _ in range(N)]
    for i in range(N):  # 인접 4칸 중 번식 가능 칸에만 나무 번식
        for j in range(N):
            if tree[i][j] > 0:
                num = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]

                    if in_range(nx, ny) and (tree[nx][ny] == 0 and treekiller[nx][ny] == 0):
                        num += 1

                if num > 0:
                    for k in range(4):
                        nx, ny = i + dx[k], j + dy[k]

                        if in_range(nx, ny) and (tree[nx][ny] == 0 and treekiller[nx][ny] == 0):
                            temp[nx][ny] += tree[i][j] // num

    for i in range(N):  # 동시에 번식
        for j in range(N):
            if temp[i][j] > 0 and treekiller[i][j] == 0:
                tree[i][j] += temp[i][j]


def spread():
    global ans
    max_loc = (N+1, N+1)
    max_tree = -1

    for i in range(N-1, -1, -1):  # 인접 4칸 중 번식 가능 칸에만 나무 번식
        for j in range(N-1, -1, -1):
            num = 0
            if tree[i][j] > 0:
                num += tree[i][j]

                for k in range(4):
                    for time in range(1, K+1):
                        nx, ny = i + ddx[k] * time, j + ddy[k] * time

                        if not in_range(nx, ny) or tree[nx][ny] <= 0:
                            break

                        num += tree[nx][ny]

            if max_tree <= num:
                max_loc = (i, j)
                max_tree = num

    if max_tree != -1:
        ans += max_tree

        tree[max_loc[0]][max_loc[1]] = 0
        treekiller[max_loc[0]][max_loc[1]] = C + 1

        for k in range(4):
            for time in range(1, K+1):
                nx, ny = max_loc[0] + ddx[k] * time, max_loc[1] + ddy[k] * time

                if not in_range(nx, ny) or tree[nx][ny] == -1:
                    break

                if tree[nx][ny] == 0:
                    treekiller[nx][ny] = C+1
                    break

                tree[nx][ny] = 0
                treekiller[nx][ny] = C+1


for _ in range(M):  # m년
    # print(f"{_+1} year: ")
    for i in range(N):  # 1년이 지난 후 제초제 감소
        for j in range(N):
            if treekiller[i][j] > 0:
                treekiller[i][j] -= 1

    grow()
    # print("after grow")
    # for t in tree:
    #     print(t)

    breed()
    # print("after breed")
    # for t in tree:
    #     print(t)

    spread()
    # print("after spread")
    # for t in tree:
    #     print(t)

    # print()
    # print(f"tree killed: {ans}")
    # print()

print(ans)
