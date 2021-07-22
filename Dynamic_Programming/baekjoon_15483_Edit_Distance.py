import sys


# Minimum Edit
def solution(str_a, str_b):
    table = [[0] * (len(str_a)+1) for _ in range(len(str_b)+1)]
    table[0] = [i for i in range(len(str_a)+1)]
    for i in range(len(str_b)+1):
        table[i][0] = i
    for i in range(1, len(str_b)+1):
        for j in range(1, len(str_a)+1):
            if str_a[j-1] == str_b[i-1]:
                table[i][j] = table[i-1][j-1]
                continue
            table[i][j] = min(table[i-1][j], table[i][j-1], table[i-1][j-1]) + 1
    return table[-1][-1]


if __name__ == "__main__":
    str1 = sys.stdin.readline().rstrip()
    str2 = sys.stdin.readline().rstrip()
    print(solution(str1, str2))
