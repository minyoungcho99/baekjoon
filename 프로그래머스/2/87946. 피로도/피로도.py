
result = []
max_n = 0


def backtrack(k, dungeons):
    global max_n

    max_n = max(max_n, len(result))

    for i in range(len(dungeons)):
        if i not in result and dungeons[i][0] <= k: 
            result.append(i)
            backtrack(k - dungeons[i][1], dungeons) 
            result.pop()


def solution(k, dungeons):
    backtrack(k, dungeons)
    return max_n