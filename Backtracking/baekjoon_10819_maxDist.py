import sys


def get_sum(s):
    li = s.split()
    _sum = 0
    for i in range(1, len(li)):
        _sum += abs(int(li[i]) - int(li[i-1]))
    return _sum


def recur(que, depth, max_depth, visited):
    global answer
    if depth == max_depth:
        tmp = get_sum(que)
        answer = tmp if tmp > answer else answer
        return
    for i in range(max_depth):
        if not visited[i]:
            visited[i] = True
            recur(que + " " + str(seq[i]), depth+1, max_depth, visited)
            visited[i] = False


def solution(n):
    visited = [False] * n
    recur("", 0, n, visited)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    answer = 0
    seq = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N)
    print(answer)
