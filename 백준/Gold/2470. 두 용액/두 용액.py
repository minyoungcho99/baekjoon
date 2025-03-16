# 두 용액
import sys


def find_mut():
    min_diff = float('inf')
    min_liq = (0, 0)
    st = 0
    en = N - 1

    while st < en:
        tmp = liq[st] + liq[en]
        if abs(tmp) < min_diff:
            min_diff = abs(tmp)
            min_liq = (liq[st], liq[en])

        elif tmp < 0:
            st += 1

        else:
            en -= 1

    return min_liq

N = int(sys.stdin.readline())
liq = list(map(int, sys.stdin.readline().split()))
liq.sort()

print(" ".join(map(str, find_mut())))