import sys


def in_range(x):
    return 0 < x <= 50


N = int(sys.stdin.readline())
if in_range(N) and N % 2 == 1:
    tri = [[] for _ in range(N)]
    num = 0
    
    for i in range(N):
        for _ in range(i+1):
            num += 1
            tri[i].append(num)
        if i % 2 != 0:
            tri[i] = tri[i][::-1]
    
    for t in tri:
        print(" ".join(map(str, t)))
        
else:
    print("INPUT ERROR!")
