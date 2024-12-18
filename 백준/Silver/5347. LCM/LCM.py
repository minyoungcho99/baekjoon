# LCM
import sys

N = int(sys.stdin.readline())

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())

    print(A * B // gcd(A, B))