import sys


def is_multiple(a, b):
    if a % b == 0:
        return True
    return False


def is_factor(a, b):
    if b % a == 0:
        return True
    return False


def solution(a, b):
    if is_multiple(a, b):
        return 'multiple'
    if is_factor(a, b):
        return 'factor'
    return 'neither'


if __name__ == "__main__":
    while True:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if a == 0 and b == 0:
            break
        print(solution(a, b))
