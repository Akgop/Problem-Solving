import sys


def floyd(n):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


def get_minimum_cycle(n):
    minimum = INF
    for i in range(1, n + 1):
        if graph[i][i] != INF:
            minimum = min(minimum, graph[i][i])
    return minimum


def solution(n):
    floyd(n)
    answer = get_minimum_cycle(n)
    return answer if answer < INF else -1


if __name__ == "__main__":
    INF = int(1e9)
    V, E = map(int, sys.stdin.readline().rstrip().split())
    graph = [[INF] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        A, B, Cost = map(int, sys.stdin.readline().rstrip().split())
        graph[A][B] = Cost
    print(solution(V))
