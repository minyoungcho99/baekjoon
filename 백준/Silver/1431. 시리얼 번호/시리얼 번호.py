# 시리얼 번호
import sys
from functools import cmp_to_key

N = int(sys.stdin.readline())
words = []

for _ in range(N):
    words.append(sys.stdin.readline().strip())


def comparator(a, b):
    total_a = 0
    total_b = 0

    for i in a:
        if i in '1234567890':
            total_a += int(i)

    for i in b:
        if i in '1234567890':
            total_b += int(i)

    if total_a > total_b:
        return 1
    elif total_a < total_b:
        return -1
    else:
        return 0


words.sort()
words.sort(key=cmp_to_key(comparator))
words.sort(key=lambda x: len(x))

for w in words:
    print(w)