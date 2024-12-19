# 차집합
import sys

NA, NB = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

result = A - B

print(len(result))
if result:
    print(" ".join(map(str, sorted(result))))
