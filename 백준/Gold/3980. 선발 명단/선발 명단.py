# 선발 명단
import sys


def dfs(depth, score):
    global max_ab

    if depth == 11:
        max_ab = max(max_ab, score)
        return

    for pos in range(11):
        if not visited[pos] and r[depth][pos] > 0:
            visited[pos] = True
            dfs(depth + 1, score + r[depth][pos])
            visited[pos] = False


C = int(sys.stdin.readline())

for _ in range(C):
    r = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
    max_ab = float('-inf')
    visited = [False] * 11
    dfs(0, 0)
    print(max_ab)