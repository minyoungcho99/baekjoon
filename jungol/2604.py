import sys

stri = sys.stdin.readline().rstrip()

h = 10
before = stri[0]

for i in range(1, len(stri)):
    now = stri[i]

    if before == now:
        h += 5
    else:
        before = now
        h += 10

print(h)
