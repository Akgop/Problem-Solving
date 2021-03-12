import sys

INF = int(1e9)


def floyd(n):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


def solution(n, m):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0
    floyd(n)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == INF:
                print(0, end=' ')
            else:
                print(graph[i][j], end=' ')
        print()


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b, cost = map(int, sys.stdin.readline().rstrip().split())
        graph[a][b] = min(graph[a][b], cost)
    solution(N, M)

