import sys
from collections import defaultdict

T = int(sys.stdin.readline())

for _ in range(T):
    ans = 1
    dct = defaultdict(list)
    N = int(sys.stdin.readline())
    for _ in range(N):
        a, b = sys.stdin.readline().rstrip().split()
        
        if a not in dct[b]:
            dct[b].append(a)

    for d in dct.values():
        ans *= len(d) + 1
    print(ans - 1)
