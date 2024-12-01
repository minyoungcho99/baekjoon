# 로또
import sys
result = []

def backtrack(result):
    if len(result) == 6:
        print(" ".join(map(str, result)))
        return

    for n in nums:
        if n not in result:
            try:
                if result[-1] < n:
                    result.append(n)
                    backtrack(result)
                    result.pop()

            except:
                result.append(n)
                backtrack(result)
                result.pop()


while True:
    nums = list(map(int, sys.stdin.readline().split()))
    k = nums[0]

    if k == 0:
        break
    nums = nums[1:]

    backtrack([])
    print()