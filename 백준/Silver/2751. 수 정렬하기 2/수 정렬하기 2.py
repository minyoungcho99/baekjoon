# 수 정렬하기 2
import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))


for i in sorted(nums):
    print(i)