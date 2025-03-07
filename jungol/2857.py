import sys

word = []
max_length = 0

while True:
    line = list(sys.stdin.readline().rstrip())
    if not line:
        break

    word.append(line)
    max_length = max(max_length, len(line))

for j in range(max_length):
    for i in range(len(word)):
        try:
            print(word[i][j], end='')
        except:
            continue
