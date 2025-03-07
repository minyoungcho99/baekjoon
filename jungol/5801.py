import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([i for i in range(N, 0, -1)])

ans = []
while q:
    if q:
        ans.append(q.pop())
    if q:
        q.appendleft(q.pop())

print(" ".join(map(str, ans)))
