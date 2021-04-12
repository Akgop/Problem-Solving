def solution(N, stages):
    answer = []

    # 카운트 정렬
    count = [0] * (N + 2)
    for stage in stages:    # O(len(stages)): 20 만
        count[stage] += 1

    total = len(stages)     # 사람 수 세줌
    for i in range(1, N + 1):   # O(N): 500
        if total == 0:
            answer.append((0.0, i))
            continue
        tmp = count[i] / total
        answer.append((tmp, i))
        total -= count[i]

    # O(NlogN) -> 500 * log 500
    answer.sort(key=lambda x: x[0], reverse=True)
    result = []
    for a in answer:
        result.append(a[1])

    return result


print(solution(
    5, [2, 1, 2, 6, 2, 4, 3, 3]
))

print(solution(
    4, [4,4,4,4,4]
))

# 나누기 0에 대한 에러 처리
print(solution(
    5, [3]
))