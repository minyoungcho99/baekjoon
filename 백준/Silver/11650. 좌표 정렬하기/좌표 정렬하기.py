# 좌표 정렬하기
import sys

N = int(sys.stdin.readline())
crds = []

for _ in range(N):
    crds.append(tuple(map(int, sys.stdin.readline().split())))

for x, y in sorted(crds):
    print(x, y)