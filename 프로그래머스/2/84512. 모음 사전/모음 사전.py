# 모음 사전
result = []
words = []

def backtrack(word, cnt):
    temp_word = "".join(map(str, result))

    words.append(temp_word)

    for i in ['A', 'E', 'I', 'O', 'U']:
        result.append(i)
        if cnt <= 4:
            backtrack(word, cnt+1)
        result.pop()


def solution(word):
    backtrack(word, 0)
    words.sort()

    return words.index(word)