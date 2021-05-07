import sys


# LCS
def solution(str_a, str_b):
    n = len(str_a)
    m = len(str_b)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str_a[i - 1] == str_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[n][m]


print(solution("cat", "cut"))
print(solution("sunday", "saturday"))
print(solution("aaawzawzaaaacc", "axxdddddddddc"))
print(solution("aaawdawdaaaacc", "axxddddddddddc"))
print(solution("banana", "baanana"))