# 숫자 카드 2
import sys
from collections import Counter

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

cnt = Counter(A)

for i in range(M):
    print(cnt[B[i]], end = ' ')