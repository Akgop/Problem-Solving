import sys


def recur(answer, depth, n, m, visited):
    if depth == m:
        print(answer.lstrip())
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            recur(answer + " " + str(seq[i]), depth + 1, n, m, visited)
            visited[i] = False


def solution(n, m):
    seq.sort()
    visited = [False] * n
    answer = ""
    recur(answer, 0, n, m, visited)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    seq = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, M)
