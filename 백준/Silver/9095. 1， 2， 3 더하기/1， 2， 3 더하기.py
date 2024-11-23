# 1, 2, 3 더하기
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    
    if N == 1:
        print(1)
    
    elif N == 2:
        print(2)
        
    elif N == 3:
        print(4)
        
    else:
        D = [0] * (N + 1)
        D[1], D[2], D[3] = 1, 2, 4
    
        for i in range(4, N+1):
            D[i] = D[i-1] + D[i-2] + D[i-3]
    
        print(D[N])