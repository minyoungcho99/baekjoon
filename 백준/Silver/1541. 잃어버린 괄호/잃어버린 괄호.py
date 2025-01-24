# 잃어버린 괄호
import sys

S = sys.stdin.readline().rstrip()
eqs = []
temp = ''
sign = 1
ans = 0

for idx in range(len(S)):
    if S[idx] not in '+-':
        temp += S[idx]
    else:
        eqs.append(int(temp))
        eqs.append(S[idx])
        temp = ''

eqs.append(int(temp))


for idx in range(len(eqs)):
    if type(eqs[idx]) == int:  # 숫자일 때
        if sign == 1:
            ans += eqs[idx]

        else:
            ans += -eqs[idx]

    else:  # 부호일 때
        if sign == 1 and eqs[idx] == '-':
            sign = -1

print(ans)