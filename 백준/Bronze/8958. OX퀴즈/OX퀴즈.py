# OX퀴즈
import sys

N = int(sys.stdin.readline())

for _ in range(N):
    quiz = sys.stdin.readline()

    cnt = 0
    score = 0

    for q in quiz:
        if q == 'O':
            cnt += 1
            score += cnt

        else:
            cnt = 0

    print(score)