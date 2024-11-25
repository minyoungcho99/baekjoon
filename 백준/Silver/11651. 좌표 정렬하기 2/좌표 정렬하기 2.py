# 좌표 정렬하기 2
import sys

N = int(sys.stdin.readline())
crds = []

for _ in range(N):
    crds.append(tuple(map(int, sys.stdin.readline().split())))

for x, y in sorted(crds, key=lambda z: (z[1], z[0])):
    print(x, y)