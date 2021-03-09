import sys


def solution(numbers, targets, n, m):
    for target in targets:
        if numbers[target] == 1:
            print("yes", end=' ')
        else:
            print("no", end=' ')


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    Numbers = [0] * 1000000
    for i in sys.stdin.readline().rstrip().split():
        Numbers[int(i)] = 1
    M = int(sys.stdin.readline().rstrip())
    Targets = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(Numbers, Targets, N, M)
