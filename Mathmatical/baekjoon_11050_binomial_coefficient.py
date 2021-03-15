import sys


# def binomial_coefficient(n, k):
#     if k == 0 or k == n:
#         return 1
#     return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)


def binomial_coefficient(n, k):
    if k == 0 or k == n:
        memoization[n][k] = 1
        return memoization[n][k]
    if memoization[n-1][k-1] == 0:
        memoization[n-1][k-1] = binomial_coefficient(n-1, k-1)
    if memoization[n-1][k] == 0:
        memoization[n-1][k] = binomial_coefficient(n-1, k)
    return memoization[n-1][k-1] + memoization[n-1][k]


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    memoization = [[0]*(K+1) for _ in range(N+1)]
    print(binomial_coefficient(N, K))
