# 프로세스
from collections import deque

def solution(priorities, location):
    ans = [0] * len(priorities)
    pr = []

    for p in enumerate(priorities):
        pr.append(p)

    q = deque(pr)
    temp = 1

    while q:
        top = q.popleft()
        less = False

        for i in q:
            if i[1] > top[1]:
                q.append(top)
                less = True
                break

        if not less:
            ans[top[0]] = temp
            temp += 1

        if ans[location] != 0:
            break

    return ans[location]