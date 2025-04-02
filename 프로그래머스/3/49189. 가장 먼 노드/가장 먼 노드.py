import heapq

def solution(n, edge):
    adj_list = [[] for _ in range(n+1)]
    best = [float('inf')] * (n+1)
    
    for a, b in edge:
        adj_list[a].append((b, 1))
        adj_list[b].append((a, 1))
    
    pq = []
    heapq.heappush(pq, (0, 1))
    best[1] = 0
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        if best[node] < dist:
            continue
        
        for cand_node, cand_dist in adj_list[node]:
            if dist + cand_dist < best[cand_node]:
                best[cand_node] = dist + cand_dist
                heapq.heappush(pq, (dist + cand_dist, cand_node))
    
    max_dist = 0
    cnt = 0
    for b in best: 
        if type(b) != float:
            if max_dist < b:
                max_dist = b
                cnt = 1
                
            elif max_dist == b:
                cnt += 1
            
    return cnt