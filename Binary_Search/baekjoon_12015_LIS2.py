import sys
from bisect import bisect_left


def solution():
    result = [0]
    for s in seq:
        if result[-1] < s:
            result.append(s)
        else:
            result[bisect_left(result, s)] = s
    return len(result) - 1


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    seq = [i for i in map(int, sys.stdin.readline().rstrip().split())]
    print(solution())
