import sys


def floyd(v):
    for i in range(1, v + 1):
        graph[i][i] = 0
    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if graph[i][j] == int(1e9):
                graph[i][j] = 0
            print(graph[i][j], end=' ')
        print()


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        graph[a][b] = min(c, graph[a][b])
    floyd(N)
