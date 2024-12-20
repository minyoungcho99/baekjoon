# 소수 찾기
from itertools import permutations
from math import sqrt

def solution(numbers):
    nums = list(map(int, numbers))
    ans = 0
    num_list = []

    def is_prime(num):
        if num <= 1:
            return False

        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False

        return True

    for i in range(1, len(nums) + 1):
        for j in permutations(nums, i):
            try:
                num = int("".join(map(str, j)))
                if num not in num_list:
                    num_list.append(num)

            except:
                continue


    for num in num_list:
        if is_prime(num):
            ans += 1

    return ans