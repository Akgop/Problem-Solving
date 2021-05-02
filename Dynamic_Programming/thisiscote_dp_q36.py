import sys


# LCS
def solution(str_a, str_b):
    table = [[0] * (len(str_b) + 1) for _ in range(len(str_a) + 1)]

    for i in range(1, len(str_a) + 1):
        for j in range(1, len(str_b) + 1):
            if str_a[i - 1] == str_b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return max(len(str_a), len(str_b)) - table[len(str_a)][len(str_b)]


print(solution("cat", "cut"))
print(solution("sunday", "saturday"))
