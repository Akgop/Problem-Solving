import sys


def solution(n, w, load, trucks):
    # 변수 초기화
    t_len = len(trucks)
    timer = [0] * t_len
    answer = 0
    cur_capacity = trucks[0]
    timer[0] = 1
    # head 는 다음에 추가 할 트럭의 index
    # tail 은 다음에 빼야 할 트럭의 index
    head, tail = 0, 0
    while tail < t_len:
        # 0. 1초 흐름
        answer += 1  # 1초 늘려
        # 1. 트럭이 다리를 다 지나간 상황
        if timer[tail] + w <= answer:
            cur_capacity -= trucks[tail]
            tail += 1
        # 2. 더이상 올라올 트럭이 없음
        if head + 1 >= t_len:
            continue
        # 3. 트럭이 다리에 더 올라올 수 있는 상황
        if cur_capacity + trucks[head + 1] <= load:
            cur_capacity += trucks[head + 1]
            timer[head + 1] = answer
            head += 1

    return answer


if __name__ == "__main__":
    N, W, L = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(N, W, L, A))
