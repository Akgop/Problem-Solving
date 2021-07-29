def solution(bridge_length, weight, truck_weights):
    time, head, tail, cur_weight = 0, 0, 0, 0
    entry_time = [0] * len(truck_weights)
    while head < len(truck_weights):
        time += 1
        # 나가야 할 트럭이 있다면
        if entry_time[tail] + bridge_length == time:
            cur_weight -= truck_weights[tail]
            tail += 1
        if head >= len(truck_weights):
            continue
        # 트럭이 다리에 새로 입장해도 넘치지 않는다면
        if cur_weight + truck_weights[head] <= weight:
            entry_time[head] = time
            cur_weight += truck_weights[head]
            head += 1
    return time + bridge_length


print(solution(10000, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
