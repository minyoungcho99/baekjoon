# 암호 만들기
import sys

L, C = map(int, sys.stdin.readline().split())
alph = list(sys.stdin.readline().rstrip().split())


def vowel(temp):
    cnt = 0
    for t in temp:
        if t in "aeiou":
            cnt += 1

    return cnt


def combination(temp, d):
    if len(temp) == L:
        v = vowel(temp)
        if v >= 1 and L - v >= 2:
            print("".join(map(str, temp)))

        return

    for idx in range(d, C):
        combination(temp + [alph[idx]], idx+1)


alph.sort()
combination([], 0)
