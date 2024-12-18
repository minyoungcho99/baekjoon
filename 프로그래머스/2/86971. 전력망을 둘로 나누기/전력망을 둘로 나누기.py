# 전력망을 둘로 나누기
from collections import deque
from copy import deepcopy

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    min_diff = float('inf')

    for w1, w2 in wires:
        graph[w1].append(w2)
        graph[w2].append(w1)

    def bfs(start):
        visited[start] = True
        cnt = 1
        q = deque([start])

        while q:
            node = q.popleft()

            for adj in temp_graph[node]:
                if not visited[adj]:
                    visited[adj] = True
                    cnt += 1
                    q.append(adj)

        return cnt

    for i in range(len(graph)):
        if graph[i]:
            for j in range(len(graph[i])):
                temp_graph = deepcopy(graph)

                a = temp_graph[i][j]
                temp_graph[a].remove(i)
                temp_graph[i].remove(a)

                visited = [False] * (n+1)

                diff_i = bfs(i)
                diff_j = bfs(a)

                if abs(diff_i - diff_j) < min_diff:
                    min_diff = abs(diff_i - diff_j)

    return min_diff

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))