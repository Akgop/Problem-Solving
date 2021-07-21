import sys


def dp(n, k):
    table = [[0]*(n+1) for _ in range(k+1)]
    for i in range(n+1):
        table[1][i] = 1

    for height in range(2, k+1):
        for i in range(n+1):
            table[height][i] = (sum(table[height-1][:i+1]) % INF)

    return table[k][n]


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    INF = int(1e9)
    print(dp(N, K))
