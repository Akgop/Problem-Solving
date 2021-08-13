import sys
from math import lcm


def solution(m, n, x, y):
    max_count = lcm(m, n)
    x, y = x - 1, y - 1
    count = x + 1
    cur_y = x % n
    while count <= max_count:
        if y == cur_y:
            break
        count += m
        cur_y = (cur_y + m) % n
    return count if count <= max_count else -1


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        M, N, X, Y = map(int, sys.stdin.readline().rstrip().split())
        print(solution(M, N, X, Y))

