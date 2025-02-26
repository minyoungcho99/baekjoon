# 먹을 것인가 먹힐 것인가
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    cnt = 0
    N, M = map(int, sys.stdin.readline().split())
    al = list(map(int, sys.stdin.readline().split()))
    bl = list(map(int, sys.stdin.readline().split()))

    al.sort()
    bl.sort()
    for a in al:
        for b in bl:
            if a <= b:
                break

            else:
                cnt += 1

    print(cnt)