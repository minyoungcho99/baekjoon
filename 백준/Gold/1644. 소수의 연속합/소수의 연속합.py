# 소수의 연속합
import sys

N = int(sys.stdin.readline())
nums = []

for i in range(2, N+1):
    temp = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            temp = False
            break

    if temp:
        nums.append(i)

if not nums:
    print(0)
else:
    total = nums[0]
    en = 0
    ans = 0

    for st in range(len(nums)):
        while en != len(nums) - 1 and total < N:
            en += 1
            total += nums[en]
    
        if total == N:
            ans += 1

        total -= nums[st]

    print(ans)