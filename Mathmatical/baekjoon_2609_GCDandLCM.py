import sys
from math import gcd


def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def get_lcm(a, b):
    return a * b // get_gcd(a, b)


if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().rstrip().split())
    # print(gcd(a, b))
    # print(a*b//gcd(a, b))
    print(get_gcd(a, b))
    print(get_lcm(a, b))
