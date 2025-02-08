import sys
from collections import defaultdict

S, P = map(int, sys.stdin.readline().split())
seq = list(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split())) 

cnt = defaultdict(int) 
ans = 0

def check():
    return cnt["A"] >= num[0] and cnt["C"] >= num[1] and cnt["G"] >= num[2] and cnt["T"] >= num[3]

for i in range(P):
    cnt[seq[i]] += 1

if check():
    ans += 1

for pt in range(1, S - P + 1):
    cnt[seq[pt - 1]] -= 1 
    cnt[seq[pt + P - 1]] += 1  

    if check():
        ans += 1

print(ans)