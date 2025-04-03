def solution(n, wires):
    def dfs(start):
        visited[start] = True 
        cnt = 1
        
        for adj in adj_list[start]:
            if not visited[adj]:
                cnt += dfs(adj)
                
        return cnt
    
    answer = float('inf')
    
    for i in range(len(wires)):
        temp_wires = wires[:]
        temp_wires.remove(temp_wires[i])
        
        adj_list = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        
        for a, b in temp_wires:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        temp = dfs(1)
        other = n-temp
        answer = min(answer, abs(other-temp))
        
    return answer