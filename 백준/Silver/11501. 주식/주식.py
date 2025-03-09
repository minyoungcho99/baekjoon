# 주식
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    stock = list(map(int, sys.stdin.readline().split()))

    max_val = 0
    ans = 0
    for i in range(len(stock) - 1, -1, -1):
        if max_val < stock[i]:
            max_val = stock[i]

        else:
            ans += (max_val - stock[i])

    print(ans)