import sys

N = int(sys.stdin.readline())
board = [[' '] * N for _ in range(N)]
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

idx = 0
time = N
start = 0
end = N - 1

while time > 0:
    for k in range(time):
        board[start + k][end - k] = alpha[idx % 26]
        idx += 1

    start += 1
    time -= 1

for b in board:
    print(" ".join(map(str, b)))
