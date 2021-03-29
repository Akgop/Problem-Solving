from itertools import permutations


def solution(n, weak, dist):
    # 초기 설정
    w_len = len(weak)   # 취약점 개수
    weak_extended = weak + weak     # 취약점 개수 길이 2배로 늘림
    for i in range(w_len, w_len*2):     # 길이 조정
        weak_extended[i] += n

    # weak 를 순회하며 모든 경우의 수 탐색
    answer = len(dist) + 1
    for i in range(w_len):
        for workers in list(permutations(dist, len(dist))):
            count = 1   # 필요한 사람 수
            # 끝점 미리 구해놓음
            endpoint = weak_extended[i] + workers[count - 1]
            for j in range(i, w_len + i):
                # 만약 친구가 일할 수 있는 범위를 벗어난다면
                if weak_extended[j] > endpoint:
                    count += 1      # 다음 친구 데려옴
                    if count > len(dist):   # 불가능한 경우
                        break
                    endpoint = weak_extended[j] + workers[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer



print(
    solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
)

print(
    solution(12, [1, 3, 4, 9, 10], [3, 5, 7])
)

# print(
#     solution(200,
#              [1, 2, 3, 4, 5, 6, 7, 106, 113, 114, 122],
#              [1, 5, 20])
# )
