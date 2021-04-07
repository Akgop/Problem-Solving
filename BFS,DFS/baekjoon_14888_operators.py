import sys


def operate(num1, num2, cmd):
    if cmd == 0:
        num1 += num2
    if cmd == 1:
        num1 -= num2
    if cmd == 2:
        num1 *= num2
    if cmd == 3:
        if num1 * num2 < 0:
            num1 = -(abs(num1) // abs(num2))
        else:
            num1 //= num2
    return num1


def dfs(n, now, idx, op):
    # 연산 수행
    calculated = operate(now, numbers[idx], op)

    # 만약 마지막 인덱스면?
    if idx == n - 1:    # 최종 결과 저장
        # 연산 결과 저장
        pass

    # 4번 탐색하며 operator 에 남아있는 연산을 재귀 수행
    for i in range(4):
        # 남아 있으면
        if operators[i] > 0:
            # 연산값을 통해 재귀 수행
            dfs(n, calculated, idx + 1, i)


def solution(n):
    for i in range(4):
        if operators[i] > 0:
            # 최종 깊이, 연산 수행한 값, 다음 연산 인덱스, 연산 종류
            dfs(n, numbers[0], 1, i)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    operators = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N)
