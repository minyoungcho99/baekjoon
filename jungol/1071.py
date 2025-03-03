# 약수와 배수
import sys

N = int(sys.stdin.readline())
lst = map(int, sys.stdin.readline().split())
target = int(sys.stdin.readline())

a, b = 0, 0
for l in lst:
    if target % l == 0:
        a += l

    if l % target == 0:
        b += l

print(a)
print(b)
