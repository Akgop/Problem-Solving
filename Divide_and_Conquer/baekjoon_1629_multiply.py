import sys


def divide(a, b, c):
    if b == 1:
        return a % c
    tmp = divide(a, b // 2, c)
    if b % 2 == 0:
        return tmp * tmp % c
    else:
        return tmp * tmp * a % c


if __name__ == "__main__":
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    print(divide(A, B, C))
