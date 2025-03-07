import sys

N = int(sys.stdin.readline())
ans = 1


def recursion(n):
    global ans
    if n == 1:
        print("1! = 1")
        print(ans)
        return

    print(f"{n}! = {n} * {n-1}!")
    ans *= n
    recursion(n-1)

recursion(N)
