# 2xn 타일링
import sys

N = int(sys.stdin.readline())

if N == 1:
    print(1)

elif N == 2:
    print(2)

else:
    D = [0] * (N + 1)
    D[1], D[2] = 1, 2
    for i in range(3, N + 1):
        D[i] = (D[i - 1] + D[i - 2]) % 10007

    print(D[N])