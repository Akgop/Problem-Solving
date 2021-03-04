import sys


def solution(n, m, values):
    table = [10001] * (m + 1)
    table[0] = 0
    for v in values:
        for i in range(v, m + 1):
            if table[i - v] != 10001:
                table[i] = min(table[i], table[i-v] + v)
    print(table)
    if table[m] == 10001:
        return -1
    return table[m]


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    Values = list()
    for _ in range(N):
        Values.append(int(sys.stdin.readline().rstrip()))
    print(solution(N, M, Values))
