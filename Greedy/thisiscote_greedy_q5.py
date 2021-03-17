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


def solution(n, m):
    for b in balls:
        weights[b] += 1
    answer = binomial_coefficient(n, 2)
    for w in weights:
        if w >= 2:
            answer -= binomial_coefficient(w, 2)
    print(answer)

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    weights = [0] * (M + 1)
    balls = list(map(int, sys.stdin.readline().rstrip().split()))
    memo = [[0] * (N+1) for _ in range(N+1)]
    solution(N, M)
