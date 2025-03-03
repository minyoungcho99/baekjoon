# 숫자 사각형
import sys

N = int(sys.stdin.readline())
sqr = [[0] * N for _ in range(N)]

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
idx = 0

is_reversed = False
for j in range(N):
    if not is_reversed:
        for i in range(N):
            sqr[i][j] = string[idx]
            idx = (idx+1) % 26

        is_reversed = True

    else:
        for i in range(N-1, -1, -1):
            sqr[i][j] = string[idx]
            idx = (idx+1) % 26

        is_reversed = False
        
for s in sqr:
    print(" ".join(map(str, s)))
