import sys


def dp(k):
    table = [0] * (k+1)
    for w, v in knapsack:
        for i in range(k, w-1, -1):
            table[i] = max(table[i], table[i-w] + v)
    return table[-1]


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    knapsack = []
    for _ in range(N):
        knapsack.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(dp(K))
