# 꿀 아르바이트
import sys

N, M = map(int, sys.stdin.readline().split())
salary = list(map(int, sys.stdin.readline().split()))

profit = 0

for i in range(M):
    profit += salary[i]

max_profit = profit

for pt in range(1, N - M + 1):
    profit -= salary[pt-1]
    profit += salary[pt+M-1]

    max_profit = max(max_profit, profit)

print(max_profit)