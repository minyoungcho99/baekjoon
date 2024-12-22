# [level 2] 주식가격 - 42584 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42584) 

### 성능 요약

메모리: 19.4 MB, 시간: 147.12 ms

### 구분

코딩테스트 연습 > 스택／큐

### 채점결과

정확성: 66.7<br/>효율성: 33.3<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 22일 16:55:02

### 문제 설명

<p>초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한사항</h5>

<ul>
<li>prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.</li>
<li>prices의 길이는 2 이상 100,000 이하입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>prices</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 2, 3]</td>
<td>[4, 3, 1, 1, 0]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<ul>
<li>1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.</li>
<li>2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.</li>
<li>3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.</li>
<li>4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.</li>
<li>5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.</li>
</ul>

<p>※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

### 틀린 부분 

> 1. list slicing/initializing a deque for each top -> **효율성 통과 못함**
~~~python
def solution(prices):
    ans = []

    for i in range(len(prices)):
        top = prices[i]
        temp = 0
        q = deque(prices[i+1:])

        while q:
            x = q.popleft()
            if x >= top:
                temp += 1
            else:
                temp += 1
                break

        ans.append(temp)

    return ans
~~~


> 2. 같은 로직, idx로 O(n^2) 돌면 시간 초과 없이 통과
~~~python
def solution(prices):
    ans = []

    for i in range(len(prices)):
        temp = 0

        for j in range(i+1, len(prices)):
            temp += 1

            if prices[i] > prices[j]:
                break

        ans.append(temp)

    return ans
~~~


### 올바른 풀이
**stack** 사용 -> O(n)
~~~python
def solution(prices): 
    # answer을 4초, 3초, 2초, 1초, 0초...로 초기화
    ans = [i for i in range (len(prices) - 1, -1, -1)]
    
    # stack에 idx를 append하며 순회
    stack = [0]

    for i in range (1, len(prices)):
        # 주식 가격이 떨어지는 경우에 answer를 갱신
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            ans[j] = i - j

        stack.append(i)

    return ans
~~~
