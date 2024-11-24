# RGB거리
import sys

N = int(sys.stdin.readline())
RGB = []

for _ in range(N):
    RGB.append(list(map(int, sys.stdin.readline().split())))

D = [[0 for _ in range(3)] for _ in range(N+1)]

D[1][0] = RGB[0][0] # red
D[1][1] = RGB[0][1] # green
D[1][2] = RGB[0][2] # blue

if N == 1:
    print(min(D[1]))

else:
    for i in range(2, N+1):
        D[i][0] = min(D[i - 1][1], D[i - 1][2]) + RGB[i - 1][0]
        D[i][1] = min(D[i - 1][0], D[i - 1][2]) + RGB[i - 1][1]
        D[i][2] = min(D[i - 1][0], D[i - 1][1]) + RGB[i - 1][2]

    print(min(D[N]))