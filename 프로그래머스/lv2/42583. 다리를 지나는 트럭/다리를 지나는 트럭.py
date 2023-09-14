from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    answer = 0

    total_weights = 0

    while trucks:
        b = bridge.popleft()
        total_weights -= b

        truck = trucks[0]

        if total_weights + truck > weight:
            bridge.append(0)
            answer += 1
        else:
            bridge.append(truck)
            total_weights += trucks.popleft()
            answer += 1

    # trucks 덱에서 원소가 다 빠진 뒤
    # bridge 덱을 다리 길이 전체에 0만 있는 형태로 만들기
    while True:
        if bridge == deque([0 for _ in range(bridge_length)]):
            break

        else:
            bridge.popleft()
            bridge.append(0)
            answer += 1

    return answer