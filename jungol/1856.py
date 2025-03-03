# 숫자 사각형
import sys

N, M = map(int, sys.stdin.readline().split())
sqr = [[0] * M for _ in range(N)]
num = 1

for i in range(N):
    for j in range(M):
        sqr[i][j] = num
        num += 1

is_reversed = False
for s in sqr:
    if not is_reversed:
        print(" ".join(map(str, s)))
        is_reversed = True

    else:
        print(" ".join(map(str, reversed(s))))
        is_reversed = False
