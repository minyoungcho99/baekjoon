import heapq
def solution(N, road, K):
    def dijkstra():
        pq = []
        heapq.heappush(pq, (0, 0))
        best[0] = 0
        
        while pq:
            dist, node = heapq.heappop(pq)
            
            if best[node] < dist:
                continue
            
            for cand_node, cand_dist in adj_list[node]:
                if best[cand_node] > dist + cand_dist:
                    best[cand_node] = dist + cand_dist
                    heapq.heappush(pq, (dist + cand_dist, cand_node))
    
    answer = 0
    best = [float('inf')] * N 
    adj_list = [[] for _ in range(N)]
    
    for ra, rb, rw in road:
        adj_list[ra-1].append((rb-1, rw))
        adj_list[rb-1].append((ra-1, rw))
    
    dijkstra()
    
    for i in range(N):
        if best[i] <= K:
            answer += 1

    return answer