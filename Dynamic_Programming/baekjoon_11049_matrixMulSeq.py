import sys


def matrix_size_mul(num1, num2, num3):
    return num1 * num2 * num3


# Top-Down DP
def dp(row, col):
    if col - row < 2:
        return 0
    if col - row == 2:
        return matrix_size_mul(numbers[row], numbers[row+1], numbers[row+2])    # row + 2 == col

    mem[row][col] = INF
    for mid in range(row+1, col):
        if not mem[row][mid]:
            mem[row][mid] = dp(row, mid)
        if not mem[mid][col]:
            mem[mid][col] = dp(mid, col)

        mem[row][col] = min(
            mem[row][col],
            mem[row][mid] + mem[mid][col] + matrix_size_mul(numbers[row], numbers[mid], numbers[col])
        )

    return mem[row][col]


if __name__ == "__main__":
    INF = int(1e9)
    N = int(sys.stdin.readline().rstrip())
    # 매트릭스 숫자 받는 부분
    numbers = []
    r, c = map(int, sys.stdin.readline().rstrip().split())
    if N == 1:
        print(r * c)
    else:
        numbers.append(r)
        numbers.append(c)
        for _ in range(N-1):
            r, c = map(int, sys.stdin.readline().rstrip().split())
            numbers.append(c)

        # TOP-DOWN DP
        mem = [[0]*len(numbers) for _ in range(len(numbers))]
        print(dp(0, len(numbers)-1))

