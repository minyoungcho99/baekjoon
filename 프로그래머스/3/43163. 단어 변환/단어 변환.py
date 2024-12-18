# 단어 변환
from collections import deque

def solution(begin, target, words):
    visited = [0] * len(words)

    def bfs():
        q = deque([begin])

        while q:
            word = q.popleft()

            if word == target:
                return visited[words.index(target)]

            for i in range(len(words)):
                if not visited[i]:
                    cnt = 0
                    for j in range(len(words[i])):
                        if word[j] != words[i][j]:
                            cnt += 1

                    if cnt == 1:
                        q.append(words[i])

                        if word == begin:
                            visited[i] = 1
                        else:
                            visited[i] = visited[words.index(word)] + 1

        return 0

    return bfs()