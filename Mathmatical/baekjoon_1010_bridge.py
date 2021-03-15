import sys


def binomial_coefficient(n, k):
    if k == 0 or k == n:
        memo[n][k] = 1
        return memo[n][k]
    if memo[n-1][k-1] == 0:
        memo[n-1][k-1] = binomial_coefficient(n-1, k-1)
    if memo[n-1][k] == 0:
        memo[n-1][k] = binomial_coefficient(n-1, k)
    return memo[n-1][k-1] + memo[n-1][k]


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().rstrip().split())
        memo = [[0] * (N + 1) for _ in range(M + 1)]
        print(binomial_coefficient(M, N))
