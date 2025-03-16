import sys, itertools
"""
디버깅한 부분
1. combination을 재귀 백트래킹으로 구현
O(len(etc), K-5)이면 최악의 경우 C(21, 10)이기 때문에 너무 큼 
-> itertools combination 써서 조합을 더 빠르게 구현 

2. ord()와 direct address table 사용하면 더 빠르게 연산할 수 있는데, 생각해내기가 힘들거같다 ..ㅎ
"""

def count_readable_words(selected):
    selected_set = set(selected)
    readable_count = 0

    for word in words:
        if word.issubset(selected_set):
            readable_count += 1

    return readable_count

N, K = map(int, sys.stdin.readline().split())

if K < 5:
    print(0)
    sys.exit()

if K == 26:
    print(N)
    sys.exit()

essential = {'a', 'c', 'i', 'n', 't'}
words = []
extra_chars = set()

for _ in range(N):
    word = set(sys.stdin.readline().strip()[4:-4])
    words.append(word)

    for char in word:
        if char not in essential:
            extra_chars.add(char)

etc = list(extra_chars)

max_word = 0

for comb in itertools.combinations(etc, min(K-5, len(etc))):
    selected = essential.union(comb)
    max_word = max(max_word, count_readable_words(selected))

print(max_word)
