# 가장 긴 짝수 연속한 부분 수열 (large)
import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

ans = float('-inf')
en = 0


def is_odd(x):
    return x % 2 != 0


odd_cnt = 1 if is_odd(nums[0]) else 0

for st in range(N):
    while en != N - 1 and odd_cnt < K:
        en += 1

        if is_odd(nums[en]):  # 홀수
            odd_cnt += 1

    while en != N - 1 and odd_cnt == K:
        en += 1

        if is_odd(nums[en]):  # 홀수
            odd_cnt += 1

    ans = max(ans, en - st + 1 - odd_cnt)

    if st != N - 1 and is_odd(nums[st]):
        odd_cnt -= 1

print(ans)