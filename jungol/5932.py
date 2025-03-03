# 숫자 사각형
import sys

N = int(sys.stdin.readline())
sqr = [[0] * N for _ in range(N)]

for j in range(N):
    for i in range(N):
        sqr[i][j] = j+1

is_reversed = False
for s in sqr:
    if not is_reversed:
        print(" ".join(map(str, s)))
        is_reversed = True

    else:
        print(" ".join(map(str, reversed(s))))
        is_reversed = False
