# 숫자 사각형
import sys

N = int(sys.stdin.readline())
sqr = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        sqr[i][j] = (i+1) * (j+1)

for s in sqr:
    print(" ".join(map(str, s)))
