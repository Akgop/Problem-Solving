import sys


def dp(k):
    table = [0] * (k+1)
    table[0] = 1
    for coin in coins:
        for i in range(coin, k + 1):
            table[i] += table[i - coin]
    return table[k]


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    coins = []
    INF = int(1e9)
    for _ in range(N):
        tmp = int(sys.stdin.readline().rstrip())
        if tmp > 10000:
            continue
        coins.append(tmp)
    print(dp(K))
