# 국영수
import sys

N = int(sys.stdin.readline())
stu = []

for _ in range(N):
    name, k, e, m = sys.stdin.readline().strip().split()
    stu.append((name, int(k), int(e), int(m)))

stu.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for s in stu:
    print(s[0])