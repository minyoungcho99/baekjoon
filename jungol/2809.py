# 약수 
import sys, math

N = int(sys.stdin.readline())
ans = set()

for i in range(1, int(math.sqrt(N))+1):
    if N % i == 0:
        ans.add(i)
        ans.add(N//i)

print(" ".join(map(str, sorted(ans))))
