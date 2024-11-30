# 피로도

from itertools import permutations

def solution(k, dungeons):
    max_num = 0

    for order in permutations(range(len(dungeons))):
        temp = 0
        temp_k = k
        for i in order:
            if dungeons[i][0] <= temp_k:
                temp_k -= dungeons[i][1]
                temp += 1
                continue

            else:
                break

        max_num = max(max_num, temp)

    return max_num
