# 동전 2
import sys

N, K = map(int, sys.stdin.readline().split())
coin = []
dp = [float('inf')] * (K+1)

for _ in range(N):
    coin.append(int(sys.stdin.readline()))

dp[0] = 0
for i in range(1, K+1):
    for c in coin:
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i-c] + 1)

print(dp[K] if type(dp[K]) != float else -1)