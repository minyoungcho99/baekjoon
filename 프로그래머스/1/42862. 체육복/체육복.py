def solution(n, lost, reserve):
    answer = 0
    
    for l in lost:
        print(l)
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
        
        if l-1 in reserve:
            lost.remove(l)
            reserve.remove(l-1)
        elif l+1 in reserve:
            lost.remove(l)
            reserve.remove(l+1)
    
    print(lost)
    answer = n - len(lost)
    
    return answer