"""
1. 처음엔 N을 보고 O(N^2) 안될 거 같아서 pointer 두개에 mid 값으로 판단하는 건가? 생각했는데 
결국에 모든 조합에 대해서 고려해야 하기 때문에 num 배열을 N번 돌면서 target + num[st] + num[en] == 0이 되는 st와 en의 개수를 세는 게 맞겠다라고 생각했다(O(N^2)).
그리고 실제로 시간도 4초로 여유롭다.

def find_zero(i, target):
    global ans
    st = i+1
    en = N-1

    while st < en:
        if num[st] + num[en] + target == 0:
            ans += 1
            st += 1

        elif num[st] + num[en] + target < 0:
            st += 1

        else:
            en -= 1
            
여기까진 쉽게 세웠는데, 사실 합이 0이 됐을 때 포인터 처리를 어떻게 해줘야 할지 감이 안와서ㅎ 그냥 감으로 st++하면 모든 조합을 다 셀 줄 알았는데
반례: [0, 0, 0, 0, 0]일 때만 봐도 그냥 st++한다면 target=0(num[0]), st=1, en=4에서 (0, 1, 4), (0, 2, 4), (0, 3, 4)만 세고 끝난다. 
모든 조합에서는 (0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4), (0, 3, 4)까지 다 세줘야 하는데도 말이다..
항상 좀 이상한 반례나 edge case를 생각해보려고 하는 버릇을 들여야겠다. 그냥 예제 맞고 제출하면 1솔인 보장이 없다.

2. 핵심은 결국 "중복된 값의 처리"이고 생각하지 못하면 풀 수 없는 문제였다.
while num[st] == num[st+1]: st+=1 뭐 이렇게도 해봤는데 st 범위를 챙겨주기 귀찮고 en도 같이 생각해줘야 되기도 하고... 생각해보니 while st < en이고 저런 경우에 ans++ 해줘도 됐을듯 싶다.
중복된 값을 처리할 때 bisect를 사용하는 법을 배운 적이 있는데 이럴 땐 별로 생각이 안난다...ㅎ 

if num[st] + num[en] + target == 0:
    if num[st] == num[en]: # 만일 처음과 끝이 같다면 정렬되어 있기 때문에 사잇값이 있더라도 다 num[st]과 같은 값일 것이니깐 현재의 st(예시 = 1)에 대해서 가능한 en(예시 = 2, 3, 4) 조합의 개수 더해줌
        ans += en - st 

    else: # 처음과 끝이 다르다면 num[en]가 중복되어 연속된 경우를 세준다. bisect_left(num, num[en])을 사용하면 num[en]이 처음 나온 index를 반환하기 때문에 en - dup_i + 1로 중복된 num[en]만큼 조합의 개수 더해줌 
    # 예시: [-2, 0, 2, 2, 2]면 (0, 2), (0, 3), (0, 4) 요렇게 세가지 경우를 세준다.
        dup_i = bisect_left(num, num[en])
        ans += en - dup_i + 1
    st += 1 # 그리고 다음 st의 조합 탐색

완탐+투포인터+이분탐색의 어려운 문제..ㅎ 왜 골4지
"""
# 합이 0
import sys
from bisect import bisect_left


def find_zero(i, target):
    global ans
    st = i+1
    en = N-1

    while st < en:
        if num[st] + num[en] + target == 0:
            if num[st] == num[en]:
                ans += en - st

            else:
                dup_i = bisect_left(num, num[en])
                ans += en - dup_i + 1

            st += 1

        elif num[st] + num[en] + target < 0:
            st += 1

        else:
            en -= 1


ans = 0
N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
num.sort()

for i in range(N-2):
    find_zero(i, num[i])

print(ans)
