import sys
from collections import defaultdict

freq = defaultdict(int)
N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

en = 1
max_len = 0
freq[nums[0]] += 1 

for st in range(N):
    while en < N and freq[nums[en]] < K:
        freq[nums[en]] += 1
        en += 1

    max_len = max(max_len, en - st)

    freq[nums[st]] -= 1

print(max_len)