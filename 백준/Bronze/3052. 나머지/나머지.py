# 나머지
import sys
from collections import Counter

nums = []

while True:
    try:
        N = int(sys.stdin.readline().strip())
    except:
        break

    nums.append(N % 42)

print(len(Counter(nums)))