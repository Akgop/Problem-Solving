import sys


def solution(n):
    idx = 0
    flag = False
    for i in range(n-1, 0, -1):
        if seq[i] > seq[i-1]:
            idx = i-1
            flag = True
            break
    if not flag:
        return -1
    idx2 = 0
    tmp = 10001
    for i in range(idx, n):
        if seq[idx] < seq[i] < tmp:
            tmp = seq[i]
            idx2 = i
    seq[idx], seq[idx2] = seq[idx2], seq[idx]
    answer = " ".join(map(str, seq[:idx+1]))
    answer += " "
    answer += " ".join(map(str, sorted(seq[idx+1:])))
    return answer.strip()


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    seq = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(N))
