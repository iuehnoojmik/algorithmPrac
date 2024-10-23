from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_queue = deque(truck_weights)
    bridge_queue = deque([0]*bridge_length)
    current_bridge_weight = 0
    
    while truck_queue:
        current_bridge_weight -= bridge_queue.popleft()
        next_truck = truck_queue[0]
        if current_bridge_weight + next_truck <= weight:
            current_bridge_weight += truck_queue.popleft()
            bridge_queue.append(next_truck)
        else:
            bridge_queue.append(0)
        answer += 1
    
    answer += bridge_length
    
    return answer