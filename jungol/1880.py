import sys

encryption = list(sys.stdin.readline().rstrip())
encryption_upper = []

for e in encryption:
    encryption_upper.append(e.upper())

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

word = sys.stdin.readline().rstrip()

for w in word:
    if w == ' ':
        print(' ', end='')

    elif w.isupper():
        print(encryption_upper[alpha_upper.index(w)], end='')

    else:
        print(encryption[alpha.index(w)], end='')
