# 수 고르기
import sys

N, M = map(int, sys.stdin.readline().split())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort() # sort the arr

en = 0
min_diff = float('inf')

for st in range(N):
    while en != N - 1 and nums[en] - nums[st] < M:
        en += 1

    if nums[en] - nums[st] >= M:
        min_diff = min(min_diff, nums[en] - nums[st])

print(min_diff)