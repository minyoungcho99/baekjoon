# 선 긋기
import sys


def count():
    last = line[0][1]
    cnt = line[0][1] - line[0][0]

    for st, en in line[1:]:
        if st < last < en or st == last:
            cnt += en - last
            last = en

        elif st > last:
            cnt += abs(st - en)
            last = en

    return cnt


N = int(sys.stdin.readline())
line = []

for _ in range(N):
    line.append(tuple(map(int, sys.stdin.readline().split())))

line.sort()
print(count())