# 예산
import sys


def count(limit):
    res = 0
    for r in request:
        if r < limit:
            res += r
        else:
            res += limit

    return res


def binary_search(st, en):
    last = 0

    while st <= en:
        mid = (st + en) // 2
        if count(mid) <= budget:
            last = mid
            st = mid + 1

        else:
            en =  mid - 1

    return last


N = int(sys.stdin.readline())
request = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

if sum(request) <= budget:
    print(max(request))

else:
    print(binary_search(1, max(request)))