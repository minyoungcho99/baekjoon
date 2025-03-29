# 쇠막대기
import sys

def get_cnt():
    stack = []
    cnt = 0

    for i in range(len(b)):
        if b[i] == "(":
            stack.append("(")

        else:
            stack.pop()
            if b[i-1] == "(":
                cnt += len(stack)

            else:
                cnt += 1

    return cnt

b = sys.stdin.readline().rstrip()
print(get_cnt())