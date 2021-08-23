import sys


def backtrack(depth, n, cost, start, cur, visited):
    global answer
    if cost >= answer:
        return
    if depth == n:
        if graph[cur][start] == 0:
            return
        answer = min(cost + graph[cur][start], answer)
        return
    for i in range(n):
        if visited[i] or graph[cur][i] == 0:
            continue
        visited[i] = True
        backtrack(depth+1, n, cost + graph[cur][i], start, i, visited)
        visited[i] = False
    return


def solution(n):
    visited = [False] * n
    for i in range(n):
        visited[i] = True
        backtrack(1, n, 0, i, i, visited)
        visited[i] = False


if __name__ == "__main__":
    answer = int(1e9)
    N = int(sys.stdin.readline().rstrip())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N)
    print(answer)
