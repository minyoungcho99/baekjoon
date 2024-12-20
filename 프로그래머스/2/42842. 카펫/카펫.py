# 카펫

def solution(brown, yellow):
    addition = (brown + 4) // 2

    for i in range(1, addition):
        j = addition - i

        if i * j - brown == yellow:
            return [j, i]