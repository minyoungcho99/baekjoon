# 거스름돈
import sys

def count(m):
    temp = m
    ans = 0
    for c in change:
        while temp >= c:
            temp -= c
            ans += 1

        if temp == 0:
            break
    return ans


change = [500, 100, 50, 10, 5, 1]
M = 1000 - int(sys.stdin.readline())

print(count(M))