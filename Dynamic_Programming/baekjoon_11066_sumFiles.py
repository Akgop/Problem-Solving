import sys


def dp(k):
    # 초기 설정
    table = [[0]*(k+1) for _ in range(k+1)]
    acc = [0] * (k+1)
    for i in range(1, k+1):
        acc[i] = acc[i-1] + files[i-1]

    for offset in range(1, k+1):
        for i in range(1, k - offset + 1):
            x, y = i, i+offset
            table[x][y] = INF
            for mid in range(offset):
                table[x][y] = min(table[x][y], (table[x][x+mid] + table[x+1+mid][y] + acc[y] - acc[x-1]))
    return table[1][k]


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    INF = int(1e9)
    for _ in range(T):
        K = int(sys.stdin.readline().rstrip())
        files = list(map(int, sys.stdin.readline().rstrip().split()))
        print(dp(K))
