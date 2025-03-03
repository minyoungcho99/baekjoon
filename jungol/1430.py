import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

res = str(A*B*C)
cnt = [0] * 10

for r in res:
    cnt[int(r)] += 1

for c in cnt:
    print(c)
