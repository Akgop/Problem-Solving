import sys


def solution(seq, n):
    answer = 0
    positive_seq = list()
    negative_seq = list()
    for num in seq:
        if num <= 0:  # 0은 음수랑 곱하면 0이 되므로 여기에 포함
            negative_seq.append(num)
        elif num > 1:  # 1은 그냥 더하는게 곱하는거보다 크다
            positive_seq.append(num)
        else:           # 1은 그냥 더한다.
            answer += 1

    positive_seq.sort(reverse=True)
    negative_seq.sort()

    p_seq_len = len(positive_seq)
    n_seq_len = len(negative_seq)

    for i in range(1, p_seq_len, 2):
        answer += positive_seq[i] * positive_seq[i-1]
    if p_seq_len % 2 == 1:  # 배열 길이가 홀수면 마지막 원소 더함
        answer += positive_seq[-1]

    for i in range(1, n_seq_len, 2):
        answer += negative_seq[i] * negative_seq[i-1]
    if n_seq_len % 2 == 1:  # 배열 길이가 홀수면 마지막 원소 더함
        answer += negative_seq[-1]

    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    _seq = list()
    for _ in range(N):
        _seq.append(int(sys.stdin.readline().rstrip()))
    print(solution(_seq, N))
