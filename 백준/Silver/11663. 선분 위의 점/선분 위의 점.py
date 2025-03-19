# 선분 위의 점
import sys
from bisect import bisect_left, bisect_right

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    ans = bisect_right(num, b) - bisect_left(num, a)
    print(ans)