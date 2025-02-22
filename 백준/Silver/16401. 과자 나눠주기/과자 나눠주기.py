# 과자 나눠주기
import sys


def count(l):
    cnt = 0
    for c in cookie:
        while c >= l:
            c -= l
            cnt += 1

    return cnt


def binary_search(st, en, m):
    result = 0
    while st <= en:
        mid = (st + en) // 2

        if count(mid) >= m:
            st = mid + 1
            result = mid

        else:
            en = mid - 1

    return result


M, N = map(int, sys.stdin.readline().split())
cookie = list(map(int, sys.stdin.readline().split()))

print(binary_search(1, max(cookie), M))