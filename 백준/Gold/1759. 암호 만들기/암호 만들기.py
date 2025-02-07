# 암호 만들기
import sys

L, C = map(int, sys.stdin.readline().split())
a = sys.stdin.readline().split()
visited = [False] * C

a.sort()


def permutation(temp):
    if len(temp) == L:
        vo = 0
        con = 0
        for t in temp:
            if t in 'aeiou':
                vo += 1
            else:
                con += 1

        if vo >= 1 and con >= 2:
            print("".join(temp))

        return

    for idx in range(C):
        if not visited[idx]:
            if temp:
                if temp[-1] < a[idx]:
                    visited[idx] = True
                    permutation(temp + [a[idx]])
                    visited[idx] = False
            else:
                visited[idx] = True
                permutation(temp + [a[idx]])
                visited[idx] = False


permutation([])