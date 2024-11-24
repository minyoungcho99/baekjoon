# N과 M (11)
import sys

N, M = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

result = []


def sequence(num):
    if num == M:
        print(" ".join(map(str, result)))
        return

    temp = 0
    for n in nums:
        if temp != n:
            temp = n
            result.append(n)
            sequence(num+1)
            result.pop()


sequence(0)