import sys


def solution(numbers, n, m):
    _min = 2000000001
    numbers.sort()
    head, tail = 0, 0
    while True:
        tmp = numbers[head] - numbers[tail]
        if tmp == m:    # m이랑 똑같은 경우는 stop
            _min = tmp
            break
        if tmp < m:     # 만약 기준 미달이면 헤드 이동
            if head == n-1:     # head 가 끝인데 기준미달이면 종료
                break
            head += 1
        elif tmp > m:   # 기준에 부합하는 경우
            if tmp < _min:      # 기존 최소값보다 작은 경우
                _min = tmp
            tail += 1

    return _min


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    A = [0] * N
    for i in range(N):
        A[i] = int(sys.stdin.readline().rstrip())
    print(solution(A, N, M))
