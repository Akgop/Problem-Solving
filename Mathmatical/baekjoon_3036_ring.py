import sys
from math import gcd


def solution(n):
    for i in range(1, n):
        g = gcd(radius[0], radius[i])
        print(radius[0]//g, end='')
        print('/', end='')
        print(radius[i]//g)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    radius = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N)
