# 등굣길

def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    p = [[0] * m for _ in range(n)]

    for i, j in puddles:
        p[j-1][i-1] = -1

    for i in range(m):
        if p[0][i] == -1:
            break

        dp[0][i] = 1

    for j in range(n):
        if p[j][0] == -1:
            break

        dp[j][0] = 1


    for i in range(1, m):
        for j in range(1, n):
            if p[j][i] != -1:
                dp[j][i] = dp[j-1][i] + dp[j][i-1]

    return dp[n-1][m-1] % 1000000007
