# 용액
import sys


N = int(sys.stdin.readline())
liq = list(map(int, sys.stdin.readline().split()))
min_diff = float('inf')
min_liq = (None, None)
st, en = 0, N-1

while st < en:
    tmp_diff = liq[st] + liq[en]
    if min_diff > abs(tmp_diff):
        min_diff = abs(tmp_diff)
        min_liq = (liq[st], liq[en])

    if tmp_diff > 0:
        en -= 1

    else:
        st += 1

print(" ".join(map(str, min_liq)))