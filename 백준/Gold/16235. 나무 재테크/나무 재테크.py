# 나무 재테크
import sys
from collections import deque


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def spring_summer():
    for i in range(N):
        for j in range(N):
            if len(tree[i][j]) > 0:
                added_nutr = 0
                new_tree = deque()
                for _ in range(len(tree[i][j])):
                    age = tree[i][j].popleft()

                    if nutr[i][j] >= age:
                        nutr[i][j] -= age
                        new_tree.append(age+1)

                    else:
                        added_nutr += age // 2

                tree[i][j] = new_tree
                nutr[i][j] += added_nutr


def fall():
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]

    for i in range(N):
        for j in range(N):
            if len(tree[i][j]) > 0:
                for age in tree[i][j]:
                    if age % 5 == 0:
                        for k in range(8):
                            nx, ny = i + dx[k], j + dy[k]
                            if in_range(nx, ny):
                                tree[nx][ny].appendleft(1)


def winter():
    for i in range(N):
        for j in range(N):
            nutr[i][j] += A[i][j]


def count():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if len(tree[i][j]) > 0:
                for age in tree[i][j]:
                    cnt += 1

    return cnt


N, M, K = map(int, sys.stdin.readline().split())
nutr = [[5] * N for _ in range(N)]
tree = [[deque([]) for _ in range(N)] for _ in range(N)]
A = []

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

for _ in range(M):
    x, y, age = map(int, sys.stdin.readline().split())
    tree[x-1][y-1].append(age)

year = 0
while True:
    if year == K:
        break
    spring_summer()
    fall()
    winter()
    year += 1

print(count())