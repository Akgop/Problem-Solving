import sys


def floyd_warshall(n):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


def solution(n, x, k):
    floyd_warshall(n)
    answer = graph[1][k] + graph[k][x]
    if answer >= INF:
        return -1
    return answer


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    INF = int(1e9)
    graph = [[INF] * (N+1) for _ in range(N+1)]

    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if a == b:
                graph[a][b] = 0

    for _ in range(M):
        s, e = map(int, sys.stdin.readline().rstrip().split())
        graph[s][e] = 1
        graph[e][s] = 1

    X, K = map(int, sys.stdin.readline().rstrip().split())

    print(solution(N, X, K))
