import sys


def dp(n):
    # 초기화
    for i in range(1, n+1):
        table[i][i] = 1

    for i in range(1, n):
        if numbers[i] == numbers[i+1]:
            table[i][i+1] = 1

    for offset in range(2, n):
        for i in range(1, n - offset + 1):
            x, y = i, i+offset
            if numbers[x] == numbers[y] and table[x+1][y-1] == 1:
                table[x][y] = 1


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    numbers = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())
    table = [[0] * (N+1) for _ in range(N+1)]
    dp(N)
    for _ in range(M):
        S, E = map(int, sys.stdin.readline().rstrip().split())
        print(table[S][E])
