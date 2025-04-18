# 역사
import sys

def floyd_warshall():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dp[i][k] and dp[k][j]:
                    dp[i][j] = True

n, k = map(int, sys.stdin.readline().split())
dp = [[False] * (n+1) for _ in range(n+1)]

for _ in range(k): # 간선처리
    a, b = map(int, sys.stdin.readline().split())
    dp[a][b] = True

floyd_warshall()

q = int(sys.stdin.readline())
for _ in range(q):
    i, j = map(int, sys.stdin.readline().split())
    if dp[i][j]:
        print(-1)

    elif dp[j][i]:
        print(1)

    elif not dp[i][j] and not dp[j][j]:
        print(0)