import sys


def floyd(n):
    for k in range(1, n+1):
        dist[k][k] = 0
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


def solution(n):
    floyd(n)
    answer = INF
    x, y = 0, 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            rtt = 0
            for c in range(1, n+1):
                rtt += min(dist[i][c], dist[j][c])
            if rtt < answer:
                answer = rtt
                x, y = i, j
    print(x, y, answer*2)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    INF = int(1e9)
    dist = [[INF] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        dist[A][B] = 1
        dist[B][A] = 1
    solution(N)
