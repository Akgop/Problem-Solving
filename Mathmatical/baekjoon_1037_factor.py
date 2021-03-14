import sys


def solution():
    factors.sort()
    return factors[0] * factors[-1]


if __name__ == "__main__":
    cnt = int(sys.stdin.readline().rstrip())
    factors = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution())
