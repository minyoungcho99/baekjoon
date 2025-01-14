# 하노이 탑 이동 순서
import sys

N = int(sys.stdin.readline())


def hanoi(a, b, n):
    if n == 1:
        print(f"{a} {b}")
        return

    hanoi(a, 6-a-b, n-1)
    print(f"{a} {b}")
    hanoi(6-a-b, b, n-1)


print(2 ** N - 1)
hanoi(1, 3, N)