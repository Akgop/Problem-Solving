import sys


def check(target):
    tmp = list(str(target))
    for i in range(len(tmp)):
        if tmp[i] in not_working:
            return False
    return True


def move_up(target, max_value):
    count = 0
    while count <= max_value:
        if check(target):
            break
        target += 1
        count += 1
    answer = len(str(target)) + count
    return answer


def move_down(target):
    count = 0
    while target >= 0:
        if check(target):
            break
        target -= 1
        count += 1
    answer = len(str(target)) + count
    return answer if target >= 0 else int(1e9)


def solution(n):
    max_value = abs(n - 100)
    return min(move_up(n, max_value), move_down(n), max_value)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    not_working = set(map(str, sys.stdin.readline().rstrip().split()))
    print(solution(N))

