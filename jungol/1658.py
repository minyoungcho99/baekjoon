import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a


A, B = map(int, sys.stdin.readline().split())
gcd = gcd(A, B)
print(gcd)
print(int(A * B / gcd))
