"""
고친 부분
1. print(binary_search(min(request), max(request))) ->  print(binary_search(1, max(request)))
상한액이 request의 최솟값이라는 보장이 없으니 1 ~ max(request) 사이에서 이분 탐색해야 함
"""
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
