import sys


def recur(answer, depth, n, m):
    if depth == m:
        if answer not in answer_set:
            print(answer.lstrip())
            answer_set.add(answer)
        return
    for i in range(n):
        if answer and seq[i] < int(answer.split(' ')[-1]):
            continue
        recur(answer + " " + str(seq[i]), depth+1, n, m)


def solution(n, m):
    seq.sort()
    answer = ""
    recur(answer, 0, n, m)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    seq_dup = list(map(int, sys.stdin.readline().rstrip().split()))
    seq_set = set(seq_dup)
    seq = list(seq_set)
    answer_set = set()
    solution(len(seq), M)
