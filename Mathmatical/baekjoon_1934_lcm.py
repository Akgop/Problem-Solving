import sys


def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def get_lcm(a, b):
    return a * b // get_gcd(a, b)


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(get_lcm(a, b))
