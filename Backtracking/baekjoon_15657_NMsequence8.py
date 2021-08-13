import sys


def recur(answer, depth, n, m, start):
    if depth == m:
        print(answer.lstrip())
        return
    for i in range(start, n):
        recur(answer + " " + str(seq[i]), depth+1, n, m, i)


def solution(n, m):
    seq.sort()
    answer = ""
    recur(answer, 0, n, m, 0)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    seq = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, M)
