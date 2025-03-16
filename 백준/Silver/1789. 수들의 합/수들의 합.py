# 수들의 합
import sys

S = int(sys.stdin.readline())
i = 1
num = 0

while True:
    if S >= i:
        S -= i
        num += 1
        i += 1

    else:
        break

print(num)