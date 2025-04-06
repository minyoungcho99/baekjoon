def dfs(sheep, wolf):
    global possible_answer
    if sheep > wolf:
        possible_answer.append(sheep)
        
    else:
        return
    
    for p, c in edges:
        if visited[p] and not visited[c]:
            visited[c] = True
            if info[c] == 0:
                dfs(sheep+1, wolf)
                
            else:
                dfs(sheep, wolf+1)
            visited[c] = False

def solution(info, edges):
    visited = [False] * len(info)
    possible_answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            possible_answer.append(sheep)

        else:
            return

        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    dfs(sheep+1, wolf)

                else:
                    dfs(sheep, wolf+1)
                visited[c] = False
            
    visited[0] = True
    dfs(1, 0)

    return max(possible_answer)