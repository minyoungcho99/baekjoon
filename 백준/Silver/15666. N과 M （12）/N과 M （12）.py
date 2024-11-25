# N과 M (12)
import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
result = []

nums.sort()

def sequence(num):
    if num == M:
        print(" ".join(map(str, result)))
        return

    temp = 0
    for n in nums:
        if result:
            if temp != n and n >= result[-1]:
                temp = n
                result.append(n)
                sequence(num+1)
                result.pop()

        else:
            if temp != n:
                temp = n
                result.append(n)
                sequence(num + 1)
                result.pop()

sequence(0)