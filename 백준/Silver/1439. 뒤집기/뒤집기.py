# 뒤집기
import sys

S = sys.stdin.readline().rstrip()

idx = 0

zeroes = 0
ones = 0

while idx <= len(S) - 1:
    temp = S[idx]

    while True:
        idx += 1
        if idx >= len(S) or S[idx] != temp:
            break

    if temp == '0':
        zeroes += 1

    else:
        ones += 1

print(min(zeroes, ones))