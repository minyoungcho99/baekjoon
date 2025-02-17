# 암기왕
import sys

T = int(sys.stdin.readline())


def binary_search(st, en, target, note_1):
    while st <= en:
        mid = (st+en) // 2

        if note_1[mid] == target:
            return True

        elif note_1[mid] < target:
            st = mid+1

        else:
            en = mid-1

    return False


for _ in range(T):
    N = int(sys.stdin.readline())
    note_1 = list(map(int, sys.stdin.readline().split()))

    M = int(sys.stdin.readline())
    note_2 = list(map(int, sys.stdin.readline().split()))

    note_1.sort()
    for target in note_2:
        if binary_search(0, N-1, target, note_1):
            print(1)

        else:
            print(0)