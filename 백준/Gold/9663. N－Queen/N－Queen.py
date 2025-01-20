# N-Queen
import sys

N = int(sys.stdin.readline())
board = [0] * (N + 1)
cnt = 0


def is_promising(nth):
    for i in range(0, nth):
        if board[i] == board[nth] or nth - i == abs(board[i] - board[nth]):
            return False

    return True


def n_queen(nth):
    global cnt
    if nth == N:
        cnt += 1
        return

    for i in range(1, N+1):
        board[nth] = i
        if is_promising(nth):
            n_queen(nth+1)


n_queen(0)
print(cnt)