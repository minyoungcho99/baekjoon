# 계단 오르기
import sys

N = int(sys.stdin.readline())

s = []
dp = [0] * N
for _ in range(N):
    s.append(int(sys.stdin.readline()))

if N <= 2:
    print(sum(s))

else:
    dp[0] = s[0]
    dp[1] = s[0] + s[1]

    for i in range(2, N):
        dp[i] = max(dp[i-2], dp[i-3] + s[i-1]) + s[i]

    print(dp[-1])