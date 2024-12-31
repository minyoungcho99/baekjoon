# 부분합
import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

en = 0
min_len = float('inf')
total = nums[0]

for st in range(N):
    while en != N - 1 and total < S:
        en += 1
        total += nums[en]

    if total >= S:
        min_len = min(min_len, en - st + 1)

    total -= nums[st]


if min_len == float('inf'):
    print(0)
else:
    print(min_len)
