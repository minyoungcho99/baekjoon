# 회의실 배정
import sys


def assign():
    time = 0
    cnt = 0

    for st, en in meeting:
        if time <= st:
            cnt += 1
            time = en

    return cnt


N = int(sys.stdin.readline())
meeting = []

for _ in range(N):
    meeting.append(tuple(map(int, sys.stdin.readline().split())))

meeting.sort(key=lambda x:(x[1], x[0]))
print(assign())