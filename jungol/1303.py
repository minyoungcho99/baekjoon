# 숫자 사각형
import sys

N, M = map(int, sys.stdin.readline().split())
sqr = [[0] * M for _ in range(N)]
num = 1

for i in range(N):
    for j in range(M):
        sqr[i][j] = num
        num += 1

for s in sqr:
    print(" ".join(map(str, s)))
