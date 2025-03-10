# 이친수
import sys

N = int(sys.stdin.readline())

if N <= 2:
    dp = [0, 1, 1]
    print(dp[N])

else:
    for _ in range(N):
        dp = [0] * (N + 1)

        dp[1] = 1
        dp[2] = 1

        for i in range(3, N+1):
            dp[i] = dp[i-1] + dp[i-2]

    print(dp[N])