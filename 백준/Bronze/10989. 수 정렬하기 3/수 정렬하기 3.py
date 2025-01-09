# 수 정렬하기 3
import sys

N = int(sys.stdin.readline())
nums = [0 for _ in range(10001)]

# for _ in range(N):
#     nums.append(int(sys.stdin.readline()))
#
# for i in sorted(nums):
#     print(i)

for _ in range(N):
    i = int(sys.stdin.readline())
    nums[i] += 1

for i in range(len(nums)):
    if nums[i] > 0:
        for _ in range(nums[i]):
            print(i)