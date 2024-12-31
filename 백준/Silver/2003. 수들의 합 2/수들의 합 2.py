# 수들의 합 2
import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

ans = 0
en = 0
total = nums[0]

for st in range(N):
    while en != N - 1 and total < M:
        en += 1
        total += nums[en]

    if total == M:
        ans += 1

    total -= nums[st]

print(ans)