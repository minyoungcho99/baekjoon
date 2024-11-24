# 계단 오르기
import sys

N = int(sys.stdin.readline())
S = [0]
D = [0] * (N+1)

for _ in range(N):
    S.append(int(sys.stdin.readline()))

total = sum(S)

if N == 1:
    print(total)

elif N == 2:
    print(total)

else:
    D[1] = S[1]
    D[2] = S[2]
    D[3] = S[3]
    for i in range(4, N+1):
        D[i] = min(D[i-2], D[i-3]) + S[i]
    print(total - min(D[N-1], D[N-2]))