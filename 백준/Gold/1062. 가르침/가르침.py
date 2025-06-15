import sys, itertools

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
