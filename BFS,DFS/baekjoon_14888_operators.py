import sys


def dfs(n, now, idx):
    global add, sub, mul, div, min_value, max_value
    # 최종 깊이까지 내려갔으면, 연산 수행
    if n == idx:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
        return
    if add > 0:
        add -= 1
        dfs(n, now + numbers[idx], idx + 1)
        add += 1
    if sub > 0:
        sub -= 1
        dfs(n, now - numbers[idx], idx + 1)
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(n, now * numbers[idx], idx + 1)
        mul += 1
    if div > 0:
        div -= 1
        dfs(n, int(now / numbers[idx]), idx + 1)
        # now // numbers[idx] <- 이렇게 하면 안된다.
        div += 1


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    add, sub, mul, div = list(map(int, sys.stdin.readline().rstrip().split()))
    min_value, max_value = int(1e9), int(-1e9)

    dfs(N, numbers[0], 1)

    print(max_value)
    print(min_value)
