# 합이 0
import sys
from bisect import bisect_left


def find_zero(i, target):
    global ans
    st = i+1
    en = N-1

    while st < en:
        if num[st] + num[en] + target == 0:
            if num[st] == num[en]:
                ans += en - st

            else:
                dup_i = bisect_left(num, num[en])
                ans += en - dup_i + 1

            st += 1

        elif num[st] + num[en] + target < 0:
            st += 1

        else:
            en -= 1


ans = 0
N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
num.sort()

for i in range(N-2):
    find_zero(i, num[i])

print(ans)