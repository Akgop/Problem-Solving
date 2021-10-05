import sys


def solution(t, w):
    for i in range(1, t+1):
        dp[0][i] = dp[0][i-1] + 1 if jadu[i] == 1 else dp[0][i-1]

    for i in range(1, w+1):
        for j in range(1, t+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if i % 2 == 0 and jadu[j] == 1:
                dp[i][j] += 1
            elif i % 2 == 1 and jadu[j] == 2:
                dp[i][j] += 1
    return dp[-1][-1]


if __name__ == "__main__":
    T, W = map(int, sys.stdin.readline().split())
    dp = [[0] * (T+1) for _ in range(W+1)]
    jadu = [0]
    for _ in range(T):
        jadu.append(int(sys.stdin.readline().rstrip()))
    print(solution(T, W))

