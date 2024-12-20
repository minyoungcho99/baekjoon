from collections import deque 

def solution(progresses, speeds):
    time = [] 
        
    for i in range(len(progresses)):
        temp = progresses[i]
        n = 0
        while temp < 100:
            temp += speeds[i]
            n += 1
            
        time.append(n)
    
    q = deque(time)
    
    ans = []
    temp = 1
    
    top = q.popleft()
  
    print(f"top:{top}")
    while q:
        x = q.popleft()
        print(x)
        
        if x <= top:
            temp += 1
            print(temp)
            
        else: 
            ans.append(temp)
            top = x
            temp = 1
    
    if temp > 0:
        ans.append(temp)
        
    return ans