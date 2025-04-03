def solution(n, computers):
    def dfs(start):
        visited[start] = True 

        for i in range(n):
            adj = computers[start][i]
            if adj == 1 and not visited[i]:
                dfs(i)
            
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer