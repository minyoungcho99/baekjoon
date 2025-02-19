# 구간 합 구하기 5
import sys

N, M = map(int, sys.stdin.readline().split())
table = []
prefix = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))


def prefix_sum():
    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix[i][j] = table[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]


prefix_sum()
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    part_sum = prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]
    print(part_sum)