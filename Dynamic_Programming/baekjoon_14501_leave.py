import sys


def solution(table, n):
    result = [0] * (n + 2)
    if table[n][0] == 1:
        result[n] = table[n][1]
    for i in range(n-1, 0, -1):
        t, p = table[i]
        # 인덱스 범위 벗어남
        if i + t > n + 1:
            result[i] = result[i + 1]
            continue
        result[i] = max(result[i + 1], result[i + t] + p)
    return max(result)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    Table = [[0]*2 for _ in range(N + 1)]
    for idx in range(1, N+1):
        T, P = map(int, sys.stdin.readline().rstrip().split())
        Table[idx][0] = T
        Table[idx][1] = P
    print(solution(Table, N))
