# 정수 삼각형
import sys

N = int(sys.stdin.readline())
tri = []
dp = [[0] * i for i in range(1, N+1)]

for _ in range(N):
    tri.append(list(map(int, sys.stdin.readline().split())))

dp[0][0] = tri[0][0]

for i in range(1, N):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]

        elif j == len(dp[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]

        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

print(max(dp[N-1]))