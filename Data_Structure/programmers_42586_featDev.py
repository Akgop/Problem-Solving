import math


def solution(progresses, speeds):
    answer = []
    remaining_days = [0] * len(progresses)
    remaining_days[0] = math.ceil((100 - progresses[0]) / speeds[0])
    head = 0
    cnt = 1
    for i in range(1, len(progresses)):
        remaining_days[i] = math.ceil((100 - progresses[i]) / speeds[i])
        if remaining_days[head] >= remaining_days[i]:
            cnt += 1
            continue
        answer.append(cnt)
        head = i
        cnt = 1
    answer.append(cnt)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([95], [1]))