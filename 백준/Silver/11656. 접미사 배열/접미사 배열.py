# 접미사 배열
import sys

S = sys.stdin.readline().strip()
words = []

for i in range(len(S)):
    words.append(S[i:])

for w in sorted(words):
    print(w)