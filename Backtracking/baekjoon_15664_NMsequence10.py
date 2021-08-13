import sys


def recur(answer, depth, n, m, count, start):
    if depth == m:
        print(answer.lstrip())
        return
    for i in range(start, n):
        if count[seq[i]] > 0:
            count[seq[i]] -= 1
            recur(answer + " " + str(seq[i]), depth+1, n, m, count, i)
            count[seq[i]] += 1


def solution(n, m):
    seq.sort()
    count = dict()
    for s in seq_dup:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    answer = ""
    recur(answer, 0, n, m, count, 0)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    seq_dup = list(map(int, sys.stdin.readline().rstrip().split()))
    seq_set = set(seq_dup)
    seq = list(seq_set)
    solution(len(seq), M)