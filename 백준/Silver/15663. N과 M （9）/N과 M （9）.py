# N과 M (9)
import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
r = []

check = [False] * (N+1)

def sequence(num):
    if num == M:
        print(" ".join(map(str, r)))
        return

    temp = 0
    for i in range(len(nums)):
        if not check[i] and temp != nums[i]:
            check[i] = True
            r.append(nums[i])
            temp = nums[i]
            sequence(num+1)
            r.pop()
            check[i] = False

sequence(0)