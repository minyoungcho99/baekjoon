# 탑
import sys

N = int(sys.stdin.readline().rstrip())
T = list(map(int, sys.stdin.readline().split()))

ans = [0 for _ in range(N)]

stack = []

for i in range(N):
    while stack:
        if stack[-1][1] > T[i]:
            ans[i] = stack[-1][0]
            break
        else:
            stack.pop()
        
    stack.append((i + 1, T[i]))

print(' '.join(map(str, ans)))