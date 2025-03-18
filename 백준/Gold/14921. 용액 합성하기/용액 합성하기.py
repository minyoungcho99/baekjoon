# 용액 합성하기
import sys


def two_pointer(st, en):
    min_diff = float('inf')

    while st < en:
        temp_diff = liq[st] + liq[en]

        if abs(temp_diff) < abs(min_diff):
            min_diff = temp_diff

        if temp_diff <= 0:
            st += 1

        else:
            en -= 1

    return min_diff

N = int(sys.stdin.readline())
liq = list(map(int, sys.stdin.readline().split()))

print(two_pointer(0, N-1))