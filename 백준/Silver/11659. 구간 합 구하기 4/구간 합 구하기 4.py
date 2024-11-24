# 구간 합 구하기 4
import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums = [0] + nums
D = [0] * (N + 1)

for k in range(1, N + 1):
    D[k] = D[k - 1] + nums[k]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    print(D[j] - D[i - 1])