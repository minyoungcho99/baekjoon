# Z
import sys

N, R, C = map(int, sys.stdin.readline().split())


def z(n, r, c):
    if n == 0:
        return 0

    half = 2**(n-1)

    if r < half and c < half:
        return z(n - 1, r, c)

    elif r < half <= c:
        return half * half + z(n - 1, r, c - half)

    elif c < half <= r:
        return 2 * half * half + z(n - 1, r - half, c)

    else:
        return 3 * half * half + z(n - 1, r - half, c - half)


print(z(N, R, C))