# 색종이(초)
import sys

pp = [[0] * 100 for _ in range(100)]
cnt = 0

N = int(sys.stdin.readline())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    for i in range(a, a+10):
        for j in range(b, b+10):
            if pp[i][j] == 0:
                pp[i][j] = 1
                cnt += 1

print(cnt)
