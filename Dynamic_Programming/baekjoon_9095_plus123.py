import sys


def solution():
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, MAX+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    MAX = 10
    dp = [0] * (MAX+1)
    solution()
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        print(dp[N])

