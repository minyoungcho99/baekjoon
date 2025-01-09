# 수 정렬하기 4
import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))

for n in sorted(nums, reverse=True):
    print(n)