from copy import deepcopy

def solution(triangle):
    dp = deepcopy(triangle)

    for i in range(len(dp)):
        for j in range(len(dp[i])):
            dp[i][j] = 0

    dp[0][0] = triangle[0][0]
    dp[1][0], dp[1][1] = dp[0][0] + triangle[1][0], dp[0][0] + triangle[1][1]

    for i in range(2, len(dp)):
        for j in range(len(dp[i])):
            if j != 0 and j != len(triangle[i])-1: # 양 끝이 아닐 때
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

            elif j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]

            else:
                dp[i][j] = dp[i - 1][j-1] + triangle[i][j]

    return max(dp[len(triangle) - 1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))