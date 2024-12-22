# 다리를 지나는 트럭2

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque()  # 다리 위 트럭 상태 (트럭 무게, 남은 시간)
    total_weight = 0  # 현재 다리 위 트럭의 총 무게

    truck_queue = deque(truck_weights)

    while truck_queue or bridge:
        # 시간 추가
        time += 1

        # 다리의 맨 앞 트럭이 다리를 완전히 지나갔는지 확인
        if bridge and bridge[0][1] == time:
            truck_weight, _ = bridge.popleft()
            total_weight -= truck_weight

        # 새로운 트럭이 다리에 올라갈 수 있는지 확인
        if truck_queue and total_weight + truck_queue[0] <= weight:
            truck_weight = truck_queue.popleft()
            bridge.append((truck_weight, time + bridge_length))
            total_weight += truck_weight

    return time