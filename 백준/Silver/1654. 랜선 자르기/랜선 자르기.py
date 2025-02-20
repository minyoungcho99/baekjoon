# 랜선 자르기
import sys


def is_possible(length, arr):
    return sum(x // length for x in arr)


def binary_search(st, en, arr, N):
    result = 0

    while st <= en:
        mid = (st + en) // 2
        if is_possible(mid, arr) >= N:
            result = mid
            st = mid + 1
        else:
            en = mid - 1
    return result


K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]

print(binary_search(1, max(lan), lan, N))