# 피보나치 수 1
import sys

N = int(sys.stdin.readline())
# dp = [0] * (N+1)
#
# if N <= 1:
#     if N == 0:
#         print(0)
#
#     else:
#         print(1)
#
# else:
#     dp[1]=1
#
#     for i in range(2, N+1):
#         dp[i] = dp[i-1] + dp[i-2]
#
#     print(dp[N])

def fibo(n):
    if n <= 1:
        return n

    return fibo(n-1) + fibo(n-2)

print(fibo(N))
