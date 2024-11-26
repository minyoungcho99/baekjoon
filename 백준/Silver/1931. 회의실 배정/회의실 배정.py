# 회의실 배정
import sys

N = int(sys.stdin.readline())
meetings = []
ans = 0
t = 0


for _ in range(N):
    meetings.append(tuple(map(int, sys.stdin.readline().split())))

meetings.sort(key= lambda x: (x[1], x[0]))

for start, end in meetings:
    if start >= t:
        ans += 1
        t = end

print(ans)