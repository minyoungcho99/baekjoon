import sys

N = int(sys.stdin.readline())

if 1 <= N <= 100 and N % 2 == 1:
    board = [[' '] * (N//2 + 1) for _ in range(N)]
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    idx = 0
    time = 1
    start = N//2

    for j in range(N//2, -1, -1):
        for k in range(time):
            board[start+k][j] = alpha[idx % 26]
            idx += 1

        time += 2
        start -= 1

    for b in board:
        print(" ".join(map(str, b)))
        
else:
    print("INPUT ERROR")
