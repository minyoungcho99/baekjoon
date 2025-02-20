# 나무 자르기
import sys


def sum_trees(cutter, tre):
    s = 0
    for t in tre:
        if t > cutter:
            s += t-cutter

    return s


def binary_search(m, en, tre):
    st = 0
    result = 0
    while st <= en:
        mid = (st+en) // 2
        if sum_trees(mid, tre) >= m:
            result = mid
            st = mid + 1

        else:
            en = mid - 1

    return result


N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

tree.sort()
print(binary_search(M, max(tree)-1, tree))