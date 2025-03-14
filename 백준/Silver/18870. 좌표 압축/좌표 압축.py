# 좌표 압축
import sys, bisect

N = int(sys.stdin.readline())
coor = list(map(int, sys.stdin.readline().split()))
sort_coor = sorted(set(coor))

for c in coor:
    print(bisect.bisect_left(sort_coor, c), end=' ')