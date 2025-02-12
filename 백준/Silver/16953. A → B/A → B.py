# A -> B
import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())


def bfs(curr, target):
    q = deque([(curr, 1)])

    while q:
        x, t = q.popleft()
        if x == target:
            return t

        if x * 2 <= target:
            q.append((x*2, t+1))
        if x * 10 + 1 <= target:
            q.append((x * 10 + 1, t+1))

    return -1

print(bfs(A, B))