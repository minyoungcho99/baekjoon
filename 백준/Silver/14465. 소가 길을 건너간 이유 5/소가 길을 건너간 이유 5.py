# 소가 길을 건너간 이유 5
import sys
from collections import defaultdict

N, K, B = map(int, sys.stdin.readline().split())
signs = [True] * N

for _ in range(B):
    num = int(sys.stdin.readline())
    signs[num-1] = False

nums = defaultdict(int)

for i in range(K):
    nums[signs[i]] += 1

min_num = nums[False]

for pt in range(1, N - K + 1):
    nums[signs[pt-1]] -= 1
    nums[signs[pt+K-1]] += 1

    min_num = min(min_num, nums[False])

print(min_num)