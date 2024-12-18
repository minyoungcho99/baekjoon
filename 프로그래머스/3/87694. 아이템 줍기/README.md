# [level 3] 아이템 줍기 - 87694 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/87694) 

### 성능 요약

메모리: 10.6 MB, 시간: 1.39 ms

### 구분

코딩테스트 연습 > 깊이／너비 우선 탐색（DFS／BFS）

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 15일 21:53:14

### 문제 설명

<p>다음과 같은 다각형 모양 지형에서 캐릭터가 아이템을 줍기 위해 이동하려 합니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/9b96b07f-72db-4b1c-bd7a-6a9c9b8d0dc6/rect_1.png" title="" alt="rect_1.png"></p>

<p>지형은 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현하며, 캐릭터는 이 다각형의 둘레(굵은 선)를 따라서 이동합니다. </p>

<p>만약 직사각형을 겹친 후 다음과 같이 중앙에 빈 공간이 생기는 경우, 다각형의 가장 바깥쪽 테두리가 캐릭터의 이동 경로가 됩니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/38b0739b-8dd8-40d8-ac44-c71678d28d07/rect_2.png" title="" alt="rect_2.png"></p>

<p>단, 서로 다른 두 직사각형의 x축 좌표 또는 y축 좌표가 같은 경우는 없습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/ec976181-987e-494e-bb2d-0615ce16252f/rect_4.png" title="" alt="rect_4.png"></p>

<p>즉, 위 그림처럼 서로 다른 두 직사각형이 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.</p>

<p>다음 그림과 같이 지형이 2개 이상으로 분리된 경우도 없습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/7eda8d92-ebe0-4b5f-bd15-0c9dc7af3a3e/rect_3.png" title="" alt="rect_3.png"></p>

<p>한 직사각형이 다른 직사각형 안에 완전히 포함되는 경우 또한 없습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/1e178b0d-6580-4981-aae3-dd82a1b95362/rect_7.png" title="" alt="rect_7.png"></p>

<p>지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때, 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return 하도록 solution 함수를 완성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>rectangle의 세로(행) 길이는 1 이상 4 이하입니다.</li>
<li>rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.

<ul>
<li>직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.</li>
<li>서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.</li>
<li>문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.</li>
</ul></li>
<li>charcterX, charcterY는 1 이상 50 이하인 자연수입니다.

<ul>
<li>지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.</li>
</ul></li>
<li>itemX, itemY는 1 이상 50 이하인 자연수입니다.

<ul>
<li>지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.</li>
</ul></li>
<li>캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.</li>
</ul>

<hr>

<ul>
<li>전체 배점의 50%는 직사각형이 1개인 경우입니다.<br></li>
<li>전체 배점의 25%는 직사각형이 2개인 경우입니다.<br></li>
<li>전체 배점의 25%는 직사각형이 3개 또는 4개인 경우입니다.<br></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>rectangle</th>
<th>characterX</th>
<th>characterY</th>
<th>itemX</th>
<th>itemY</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]</td>
<td>1</td>
<td>3</td>
<td>7</td>
<td>8</td>
<td>17</td>
</tr>
<tr>
<td>[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]</td>
<td>9</td>
<td>7</td>
<td>6</td>
<td>1</td>
<td>11</td>
</tr>
<tr>
<td>[[1,1,5,7]]</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>7</td>
<td>9</td>
</tr>
<tr>
<td>[[2,1,7,5],[6,4,10,10]]</td>
<td>3</td>
<td>1</td>
<td>7</td>
<td>10</td>
<td>15</td>
</tr>
<tr>
<td>[[2,2,5,5],[1,3,6,4],[3,1,4,6]]</td>
<td>1</td>
<td>4</td>
<td>6</td>
<td>3</td>
<td>10</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/7b89552b-f7b6-47e7-8bbd-deaf01907f70/rect_5.png" title="" alt="rect_5.png"></p>

<p>캐릭터 위치는 (1, 3)이며, 아이템 위치는 (7, 8)입니다. 위 그림과 같이 굵은 선을 따라 이동하는 경로가 가장 짧습니다.</p>

<p>입출력 예 #2</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/ac6911d0-e386-472b-a109-2542214c8d6b/rect_6.png" title="" alt="rect_6.png"></p>

<p>캐릭터 위치는 (9, 7)이며, 아이템 위치는 (6, 1)입니다. 위 그림과 같이 굵은 선을 따라 이동하는 경로가 가장 짧습니다.</p>

<p>입출력 예 #3</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/9c47ca5c-df4b-4b2e-8c5b-faf0815de665/rect_8.png" title="" alt="rect_8.png"></p>

<p>캐릭터 위치는 (1, 1)이며, 아이템 위치는 (4, 7)입니다. 위 그림과 같이 굵은 선을 따라 이동하는 경로가 가장 짧습니다.</p>

<p>입출력 예 #4, #5</p>

<p>설명 생략</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges


### 틀린 부분 
~~~python
# 아이템 줍기
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def in_range(x, y):
        **return 0 <= x < 102 and 0 <= y < 102**

    def bfs(cx, cy, ix, iy):
        **cx *= 2**
        **cy *= 2**

        **ix *= 2**
        **iy *= 2**
        visited[cy][cx] = 1
        q = deque([(cx, cy)])

        while q:
            x, y = q.popleft()

            if (x, y) == (ix, iy):
                return **visited[y][x] // 2**

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if in_range(nx, ny) and not visited[ny][nx] and map[ny][nx] == 1:

                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx, ny))

    **map = [[0] * 102 for _ in range(102)]**
    **visited = [[0] * 102 for _ in range(102)]**

    for x1, y1, x2, y2 in rectangle: # 좌측하단 x1, y1, 우측상단 x2, y2
        **x1 *= 2**
        **y1 *= 2**

        **x2 *= 2**
        **y2 *= 2**
        # 테두리 처리
        for x in range(x1, x2+1): # 하단 가로, 상단 가로
            if map[y1][x] != 3: # 하단
                map[y1][x] = 1

            if map[y2][x] != 3: # 상단
                map[y2][x] = 1

        for y in range(y1, y2+1):
            if map[y][x1] != 3:  # 좌측
                map[y][x1] = 1

            if map[y][x2] != 3:  # 우측
                map[y][x2] = 1

        # 내부 처리
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                map[y][x] = 3

    # for m in map:
    #     print(m)

    # for v in visited:
    #     print(v)

    return bfs(characterX, characterY, itemX, itemY)
~~~

![Screenshot 2024-12-18 at 6 00 29 PM](https://github.com/user-attachments/assets/70b8e65d-a6a1-4412-9b11-3e51af210680)
https://velog.io/@leeeeeyeon/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%84%EC%9D%B4%ED%85%9C-%EC%A4%8D%EA%B8%B0

**ㄷ자 모양을 ㅁ자라고 생각하게 되는 경우를 방지하기 위해 모든 좌표/배열에 2배 해준 후 결과를 //2**
