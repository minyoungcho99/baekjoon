# A -> B
import sys
from collections import deque


def bfs(a, b):
    q = deque([(a, 1)])

    while q:
        x, cnt = q.popleft()
        if x == b:
            return cnt
        elif x < b:
            q.append((x * 2, cnt + 1))
            q.append(((int(str(x) + "1")), cnt + 1))

    return -1


A, B = map(int, sys.stdin.readline().split())
print(bfs(A, B))