# 트리 순회
import sys

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N = int(sys.stdin.readline())
lc = [None] * N
rc = [None] * N

for _ in range(N):
    curr, l, r = sys.stdin.readline().rstrip().split()
    if l != '.':
        lc[alphabet.index(curr)] = alphabet.index(l)
    if r != '.':
        rc[alphabet.index(curr)] = alphabet.index(r)


def preorder(curr):
    print(alphabet[curr], end='')
    if lc[curr] is not None:
        preorder(lc[curr])
    if rc[curr] is not None:
        preorder(rc[curr])


def inorder(curr):
    if lc[curr] is not None:
        inorder(lc[curr])
    print(alphabet[curr], end='')
    if rc[curr] is not None:
        inorder(rc[curr])


def postorder(curr):
    if lc[curr] is not None:
        postorder(lc[curr])
    if rc[curr] is not None:
        postorder(rc[curr])
    print(alphabet[curr], end='')


preorder(0)
print()
inorder(0)
print()
postorder(0)