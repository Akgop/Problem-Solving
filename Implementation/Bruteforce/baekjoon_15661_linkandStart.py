import sys


def calculate(array):
    result = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            result += graph[array[i]][array[j]] + graph[array[j]][array[i]]
    return result


def backtrack(full, depth, first, visited, n, start):
    global answer
    if depth == full:
        second = []
        for i in range(n):
            if not visited[i]:
                second.append(i)
        answer = min(answer, abs(calculate(first) - calculate(second)))
        return
    for i in range(start, n):
        # first team 에 넣어
        if visited[i]:
            continue
        first.append(i)
        visited[i] = True
        backtrack(full, depth+1, first, visited, n, i)
        first.pop()
        visited[i] = False


def solution(n):
    first = []
    visited = [False] * n
    for i in range(2, n//2+1):  # first team 인원 수
        backtrack(i, 0, first, visited, n, 0)


if __name__ == "__main__":
    answer = int(1e9)
    N = int(sys.stdin.readline().rstrip())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N)
    print(answer)
