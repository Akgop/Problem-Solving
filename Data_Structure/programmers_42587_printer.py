from collections import deque


def is_biggest(cur, q):
    for i in range(len(q)):
        if cur < q[i][0]:
            return False
    return True


def solution(priorities, location):
    answer = 1
    que = deque()
    for i in range(len(priorities)):
        que.append([priorities[i], i])
    while True:
        node, idx = que.popleft()
        if is_biggest(node, que):
            if idx == location:
                break
            answer += 1
            continue
        que.append([node, idx])
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
