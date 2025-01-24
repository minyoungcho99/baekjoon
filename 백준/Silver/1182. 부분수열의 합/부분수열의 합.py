# 부분수열의 합
import sys

ans = 0
N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))


def backtrack(temp, start):
    global ans

    if sum(temp) == S and temp != []:
        ans += 1

    for i in range(start, N):
        backtrack(temp + [nums[i]], i+1)


backtrack([], 0)
print(ans)