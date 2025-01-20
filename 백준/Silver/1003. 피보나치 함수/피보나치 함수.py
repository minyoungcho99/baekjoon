# 피보나치 수
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    fibo = [[0, 0] for _ in range(N+1)]

    fibo[0][0] = 1

    if N >= 1:
        fibo[1][1] = 1

    for i in range(2, N+1):
        fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
        fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]

    print(" ".join(map(str, fibo[N])))