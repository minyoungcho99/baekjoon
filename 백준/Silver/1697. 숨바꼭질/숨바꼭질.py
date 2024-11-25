from collections import deque

n, k = map(int, input().split())
limit = 100000
visited = [0] * (limit+ 1)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for j in (x-1, x+1, 2*x):
            if 0 <= j <= limit and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)
bfs()