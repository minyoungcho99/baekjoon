# 소인수분해
import sys

N = int(sys.stdin.readline())

for i in range(2, N + 1):
    if N == 1:
        break

    while N % i == 0:
        N //= i
        print(i)