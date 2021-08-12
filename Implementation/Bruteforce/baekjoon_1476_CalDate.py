import sys


def sub_moon(m):
    return m - 1 if m - 1 > 0 else 19


def sub_sun(s):
    return s - 1 if s - 1 > 0 else 28


def sub_earth(e):
    return e - 1 if e - 1 > 0 else 15


def solution(e, s, m):
    year = 1
    while True:
        if e == s == m == 1:
            break
        e = sub_earth(e)
        s = sub_sun(s)
        m = sub_moon(m)
        year += 1
    return year


if __name__ == "__main__":
    E, S, M = map(int, sys.stdin.readline().rstrip().split())
    print(solution(E, S, M))
