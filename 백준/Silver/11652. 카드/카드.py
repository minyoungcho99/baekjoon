# 카드
import sys
from collections import defaultdict

N = int(sys.stdin.readline())
nums = defaultdict(int)

for _ in range(N):
    nums[int(sys.stdin.readline())] += 1

nums = sorted(nums.items(), key=lambda x:(-x[1], x[0]))

print(nums[0][0])
