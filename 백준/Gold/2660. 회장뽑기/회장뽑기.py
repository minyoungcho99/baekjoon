# 회장 뽑기
import sys
from collections import deque


def check(start):
    visited = [False] * (N+1)
    visited[start] = True
    q = deque([(start, 0)])
    ans[start-1][start-1] = 1

    while q:
        x, level = q.popleft()

        for adj in adj_list[x]:
            if not visited[adj]:
                visited[adj] = True
                ans[start-1][adj-1] = level+1
                q.append((adj, level+1))


N = int(sys.stdin.readline())
adj_list = [[] for _ in range(N+1)]
ans = [[float('inf')] * (N) for _ in range(N)]

while True:
    a, b = map(int, sys.stdin.readline().split())
    if (a, b) == (-1, -1):
        break

    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(1, N+1):
    check(i)

min_r = float('inf')
min_l = []

for i in range(N):
    temp_r = max(ans[i])

    if temp_r < min_r:
        min_r = temp_r
        min_l = [i+1]

    elif temp_r == min_r:
        min_l.append(i+1)

print(" ".join(map(str, (min_r, len(min_l)))))
print(" ".join(map(str, min_l)))