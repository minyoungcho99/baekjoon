import sys
from collections import defaultdict

while True:
    line = sys.stdin.readline().rstrip().split()

    if line[0] == "END":
        break

    cnt = defaultdict(int)
    for l in line:
        cnt[l] += 1

    for k in sorted(list(cnt.keys())):
        print(f"{k} : {cnt[k]}")
