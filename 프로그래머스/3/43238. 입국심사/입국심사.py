def count(m, times):
    cnt = 0
    
    for time in times:
        cnt += (m // time)

    
    return cnt

def solution(n, times):
    answer, st, en = 0, 0, max(times) * n
    
    while st <= en:
        mid = (st + en) // 2
        cnt = count(mid, times)
        
        if cnt >= n:
            en = mid - 1
            answer = mid

        else:  
            st = mid + 1
    
    return answer