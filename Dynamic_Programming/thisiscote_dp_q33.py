import sys


def dp(n):
    result = [0] * (n + 2)
    for i in range(n, 0, -1):
        t, p = board[i]
        if (i + t) > n + 1:
            result[i] = result[i + 1]
            continue
        result[i] = max(result[i + 1], (result[i + t] + p))
    print(max(result))


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    board = [(0, 0)]
    for i in range(1, N+1):
        Ti, Pi = map(int, sys.stdin.readline().rstrip().split())
        board.append((Ti, Pi))
    dp(N)
