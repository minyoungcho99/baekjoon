# 소수 찾기
import sys, math

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
ans = 0


def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False

    return True


for n in nums:
    if is_prime(n):
        ans += 1

print(ans)