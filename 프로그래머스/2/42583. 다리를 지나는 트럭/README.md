# [level 2] 다리를 지나는 트럭 - 42583 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42583) 

### 성능 요약

메모리: 10.2 MB, 시간: 68.19 ms

### 구분

코딩테스트 연습 > 스택／큐

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 22일 18:43:17

### 문제 설명

<p>트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.</p>

<p>예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.</p>
<table class="table">
        <thead><tr>
<th>경과 시간</th>
<th>다리를 지난 트럭</th>
<th>다리를 건너는 트럭</th>
<th>대기 트럭</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>[]</td>
<td>[]</td>
<td>[7,4,5,6]</td>
</tr>
<tr>
<td>1~2</td>
<td>[]</td>
<td>[7]</td>
<td>[4,5,6]</td>
</tr>
<tr>
<td>3</td>
<td>[7]</td>
<td>[4]</td>
<td>[5,6]</td>
</tr>
<tr>
<td>4</td>
<td>[7]</td>
<td>[4,5]</td>
<td>[6]</td>
</tr>
<tr>
<td>5</td>
<td>[7,4]</td>
<td>[5]</td>
<td>[6]</td>
</tr>
<tr>
<td>6~7</td>
<td>[7,4,5]</td>
<td>[6]</td>
<td>[]</td>
</tr>
<tr>
<td>8</td>
<td>[7,4,5,6]</td>
<td>[]</td>
<td>[]</td>
</tr>
</tbody>
      </table>
<p>따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.</p>

<p>solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한 조건</h5>

<ul>
<li>bridge_length는 1 이상 10,000 이하입니다.</li>
<li>weight는 1 이상 10,000 이하입니다.</li>
<li>truck_weights의 길이는 1 이상 10,000 이하입니다.</li>
<li>모든 트럭의 무게는 1 이상 weight 이하입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>bridge_length</th>
<th>weight</th>
<th>truck_weights</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>2</td>
<td>10</td>
<td>[7,4,5,6]</td>
<td>8</td>
</tr>
<tr>
<td>100</td>
<td>100</td>
<td>[10]</td>
<td>101</td>
</tr>
<tr>
<td>100</td>
<td>100</td>
<td>[10,10,10,10,10,10,10,10,10,10]</td>
<td>110</td>
</tr>
</tbody>
      </table>
<p><a href="http://icpckorea.org/2016/ONLINE/problem.pdf" target="_blank" rel="noopener">출처</a></p>

<p>※ 공지 - 2020년 4월 06일 테스트케이스가 추가되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

### 틀린 부분 (틀린 코드)

~~~python
# 다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([])

    q = deque(truck_weights)
    bridge.append(q.popleft())
    time += 1
    print(time, bridge)

    while q:
        x = q.popleft()
        while len(bridge) + 1 > bridge_length or sum(bridge) + x > weight:
            bridge.popleft()
            time += 1

            print(time, bridge)

        bridge.append(x)
        time += 1
        print(time, bridge)

    return time + bridge_length
~~~

> 1. 초별로 올바르게 나가고 올바르게 들어와야 함 **(동시에 초별로 들어오고 나갈 수 있음)**
> 2. deque 안에서 pop할 때 다리 위의 트럭이 다리를 건너는 데 걸리는 bridge_length를 고려해야 초가 지날 때 동시에 나가기/들어오기 가능 -> deque에 **(트럭 무게, 다리를 벗어나는 시간(현재 시간 + 다리 길이))** 형식으로 append해주고 다리를 벗어나는 시간이 되면 deque에서 popleft()
> 3. popleft() 후 새로운 트럭이 올라갈 수 있으면 append, 불가능하면 시간++ 시키며 iterate
