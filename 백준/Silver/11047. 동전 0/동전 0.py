# 동전 0
import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
ans = 0

for _ in range(N):
    coins.append(int(sys.stdin.readline()))

for i in range(len(coins) - 1, -1, -1):
    if K == 0:
        break

    ans += K // coins[i]
    K %= coins[i]

print(ans)